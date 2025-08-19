from discord.ext import commands
import discord
from discord.ui import View, Button
from Items import Item
from helper import find_closest_item
from discord import app_commands
from constants import GUILD_ID, USER_NOT_LINKED
from datetime import datetime
from User import User
from helper import is_linked
from Embeds import item_refund_embed


class RefundView(View):
    def __init__(self, item:Item, user):
        super().__init__()
        self.item = item
        self.user = user

        self.yes_button = Button(label="Yes", style=discord.ButtonStyle.success)
        self.no_button = Button(label="No", style=discord.ButtonStyle.danger)
        
        self.add_item(self.yes_button)
        self.add_item(self.no_button)
        
        self.yes_button.callback = self.yes_button_callback
        self.no_button.callback = self.no_button_callback

    async def yes_button_callback(self, interaction: discord.Interaction):
        self.no_button.disabled = True
        self.yes_button.disabled = True
        self.yes_button.label = "Refund"
        self.no_button.label = "Completed"
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"Refunded {self.item.name}!",ephemeral=True)
        self.user.refund_item(self.item)
        self.stop()

    async def no_button_callback(self, interaction: discord.Interaction):
        self.no_button.disabled = True
        self.yes_button.disabled = True
        self.yes_button.label = "Refund"
        self.no_button.label = "Canceled"
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"The refund has been canceled", ephemeral=True)
        self.stop()

    async def interaction_check(self, interaction):  
        return interaction.user.id == self.user.id


class RefundCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="refund", description="Refund a item that you own.")
    @app_commands.guilds(discord.Object(id =GUILD_ID))
    async def refund(self, interaction, *, item:str):
        await interaction.response.defer(thinking=True, ephemeral=True)
        member = interaction.user
        discord_id = member.id
        if not is_linked(discord_id) :
            await interaction.followup.send(USER_NOT_LINKED, ephemeral=True)
            return
        user = User(discord_id)
        item = find_closest_item(item)
        can_refund = user.can_refund(item)
        if not can_refund[0]:
            message = can_refund[1]
            await interaction.followup.send(message, ephemeral=True)
            return
        view = RefundView(item, user)
        embed = item_refund_embed(member, item, user)
        await interaction.followup.send(embed=embed, view=view)
    
    
async def setup(bot):
    await bot.add_cog(RefundCog(bot=bot))