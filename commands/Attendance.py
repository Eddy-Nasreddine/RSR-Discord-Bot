import asyncio
from discord.ext import commands
from User import User
import discord
from discord.ui import Button, View
from discord import app_commands
from constants import GUILD_ID, ATTENDENCE_CHAT_ID, ATTENDANCE_TIMEOUT, GUILD_ID, USER_NOT_LINKED
from Embeds import embed_message_start, embed_message_end, embed_attendees, embed_op_type
from helper import *
from constants import DOCKET_AMOUNT_MAIN, DOCKET_AMOUNT_SIDE

poll_session = False
attendees = []
attendees_nick = []
op_type = None
mission_id = None
canceled = False
op_points = None


class AttendanceView(View):
    def __init__(self, interaction, bot_url, user: User):
        super().__init__(timeout=ATTENDANCE_TIMEOUT)
        self.mission_id = mission_id
        self.interaction = interaction
        self.message = None 
        self.bot_url = bot_url
        self.user = user
        self.channel = interaction.client.get_channel(ATTENDENCE_CHAT_ID)

        self.here_button = Button(label="Here", style=discord.ButtonStyle.primary)
        self.zues_button = Button(label="Here Zeus", style=discord.ButtonStyle.primary)
        self.stop_button = Button(label="Stop", style=discord.ButtonStyle.danger)

        self.add_item(self.here_button)
        self.add_item(self.zues_button)
        self.add_item(self.stop_button)

        self.here_button.callback = self.here_button_callback
        self.zues_button.callback = self.zues_button_callback
        self.stop_button.callback = self.stop_button_callback

    async def here_button_callback(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        member = interaction.user
        discord_id = member.id
        if str(self.user.id) not in open_json():
            await interaction.followup.send(
                "Unable to take attendance until you have linked your account."
            )
            return
        global poll_session, attendees, attendees_nick
        discord_nick = member.nick
        if discord_id in attendees:
            await interaction.followup.send(
                "You have already attended this session.", ephemeral=True
            )
            return
        
        await interaction.followup.send(
            "Your attendance has been taken!", ephemeral=True
        )
        attendees.append(discord_id)
        attendees_nick.append(discord_nick)
        self.user.add_points(op_points)
        self.user.add_to_total()


    async def zues_button_callback(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        member = interaction.user
        discord_id = member.id
        if str(self.user.id) not in open_json():
            await interaction.followup.send(
                "Unable to take attendance until you have linked your account."
            )
            return
        elif not is_zues(interaction.user):
            await interaction.followup.send("You do not have Zeus role", ephemeral=True)
            return
        discord_nick = member.nick
        if discord_id in attendees:
            await interaction.followup.send(
                "You have already attended this session.", ephemeral=True
            )
            return
        await interaction.followup.send(
            "Your attendance has been taken! (Double Points!)", ephemeral=True
        )
        attendees.append(discord_id)
        attendees_nick.append(discord_nick)
        self.user.add_points(op_points * 2)
        self.user.add_to_total()


    async def stop_button_callback(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        if not is_zues(interaction.user):
            await interaction.followup.send(
                "You do not have permission to start or stop attendance!"
            )
            return
        global poll_session, attendees, attendees_nick
        poll_session = False
        attendees = []
        self.here_button.label = "Attendance"
        self.zues_button.label = "Has"
        self.stop_button.label = "Ended!"
        self.here_button.disabled = True
        self.zues_button.disabled = True
        self.stop_button.disabled = True

        if self.message:
            await self.message.edit(view=self)

        await interaction.followup.send("You have stopped the attendance session.")
        embed = embed_message_end(interaction=interaction)
        await self.channel.send(embed=embed)
        embed = embed_attendees(attendees_nick)
        await self.channel.send(embed=embed)
        self.stop()

    async def on_timeout(self):
        global poll_session, attendees, attendees_nick
        poll_session = False
        attendees = []
        self.here_button.label = "Attendance"
        self.zues_button.label = "Has"
        self.stop_button.label = "Ended!"
        self.here_button.disabled = True
        self.zues_button.disabled = True
        self.stop_button.disabled = True

        if self.message:
            await self.message.edit(view=self)

        embed = embed_message_end(bot_url=self.bot_url)
        await self.channel.send(embed=embed)
        embed = embed_attendees(attendees_nick)
        await self.channel.send(embed=embed)
        self.stop()

class OPtypeView(discord.ui.View):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.message = None
        self.button_clicked = asyncio.Event()
        # Define buttons
        self.main_button = discord.ui.Button(label="Main", style=discord.ButtonStyle.primary)
        self.side_button = discord.ui.Button(label="Side", style=discord.ButtonStyle.primary)
        
        self.cancel_button = discord.ui.Button(label="Cancel", style=discord.ButtonStyle.danger)

        # Add buttons to the view
        self.add_item(self.main_button)
        self.add_item(self.side_button)
        self.add_item(self.cancel_button)

        # Assign callbacks to the buttons
        self.main_button.callback = self.main_button_callback
        self.side_button.callback = self.side_button_callback
        self.cancel_button.callback = self.cancel_button_callback
        

    async def main_button_callback(self, interaction: discord.Interaction):
        global op_points, op_type
        op_type = "Main"
        op_points = DOCKET_AMOUNT_MAIN
        self.main_button.style = discord.ButtonStyle.success
        self.side_button.style = discord.ButtonStyle.danger
        self.main_button.disabled = True
        self.side_button.disabled = True
        self.cancel_button.disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send("Main op type has been selected", ephemeral=True)
        self.button_clicked.set()
        self.stop()

    async def side_button_callback(self, interaction: discord.Interaction):
        global op_points, op_type
        op_type = "Side"
        op_points = DOCKET_AMOUNT_SIDE
        self.main_button.style = discord.ButtonStyle.danger
        self.side_button.style = discord.ButtonStyle.success
        self.main_button.disabled = True
        self.side_button.disabled = True
        self.cancel_button.disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send("Side op type has been selected", ephemeral=True)
        self.button_clicked.set()
        self.stop()

    async def cancel_button_callback(self, interaction: discord.Interaction):
        global canceled
        self.main_button.style = discord.ButtonStyle.danger
        self.side_button.style = discord.ButtonStyle.danger
        self.main_button.disabled = True
        self.side_button.disabled = True
        self.cancel_button.disabled = True
        self.side_button.label = "🛑"
        self.main_button.label = "🛑"
        self.cancel_button.label = "🛑"
        await interaction.response.edit_message(view=self)
        await interaction.followup.send("This op was canceled", ephemeral=True)
        canceled = True
        self.button_clicked.set()
        self.stop()

    async def on_timeout(self):
        global canceled
        self.main_button.style = discord.ButtonStyle.danger
        self.side_button.style = discord.ButtonStyle.danger
        self.main_button.disabled = True
        self.side_button.disabled = True
        self.cancel_button.disabled = True
        self.side_button.label = "🛑"
        self.main_button.label = "🛑"
        self.cancel_button.label = "🛑"
        await self.message.edit(view=self)
        canceled = True
        self.button_clicked.set()
        self.stop()
        
    async def interaction_check(self, interaction):  
        return interaction.user.id == self.user_id 

class AttendanceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="attendance", description="Start attendance.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def attendance(self, interaction):
        await interaction.response.defer(ephemeral=True, thinking=True)
        if not is_zues(interaction.user):
            await interaction.followup.send(
                "You do not have permission to start or stop attendance!"
            )
            return
        member = interaction.user
        user = User(member.id)
        if str(user.id) not in open_json():
            await interaction.followup.send(USER_NOT_LINKED)
            return
        global poll_session, attendees, attendees_nick, op_type, op_points, canceled
        if poll_session is True:
            await interaction.followup.send(
                "An op has already been started or the current one has not ended."
            )
            return

        view = OPtypeView(user.id)
        message = await interaction.followup.send(embed=embed_op_type(member), view=view)
        view.message = message
        await view.button_clicked.wait()
        if (canceled is True):
            canceled = False
            return  
        
        view = AttendanceView(interaction, self.bot.user.avatar.url, user)

        channel = self.bot.get_channel(ATTENDENCE_CHAT_ID)
        message = await channel.send(
            embed=embed_message_start(member, op_type), view=view
        )
        view.message = message  

        attendees = []
        attendees_nick = []
        poll_session = True

        await interaction.followup.send(
            f"Attendance has started in {channel.mention}.", ephemeral=True
        )

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


async def setup(bot):
    await bot.add_cog(AttendanceCog(bot=bot))
