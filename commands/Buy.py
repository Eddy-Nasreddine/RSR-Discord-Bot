from discord.ext import commands
from helper import *
import discord
from discord.ui import Button, View
from discord import app_commands
from datetime import datetime
from constants import GUILD_ID
from User import User
from Items import Item
from Embeds import ItemEmbed
from helper import find_closest_item

class RequestView(View):
    def __init__(self, user: User, item: Item, can_buy):
        super().__init__()
        self.item = item
        self.user= user
        self.can_buy = can_buy
        self.yes_button = discord.ui.Button(label="Yes", style=discord.ButtonStyle.success)
        self.no_button = discord.ui.Button(label="No", style=discord.ButtonStyle.danger)
        self.add_item(self.yes_button)
        self.add_item(self.no_button)
        self.yes_button.callback = self.yes_button_callback
        self.no_button.callback = self.no_button_callback
        
    async def interaction_check(self, interaction):  
        return interaction.user.id == self.user.id
    
    async def yes_button_callback(self, interaction:discord.Interaction):
        labels = ["Purchase", "Completed"]
        did_buy = False
        if not self.can_buy[0]:
            message = self.can_buy[1]
            labels[1] = "Canceled"
        else:
            message = f"Purchased {self.item.name}!"
            did_buy = True
        self.yes_button.disabled = True
        self.no_button.disabled = True
        self.yes_button.label = labels[0]
        self.no_button.label = labels[1]
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(message, ephemeral=True)
        if did_buy:
            self.user.buy_item(self.item)
        self.stop()

    async def no_button_callback(self,  interaction:discord.Interaction):
        self.yes_button.disabled = True
        self.no_button.disabled = True
        self.yes_button.label = "Purchase"
        self.no_button.label = "Canceled"
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"If this was not the item you wanted try again and give a more accurate item description", ephemeral=True)
        self.stop()

      
class RequestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="request", description="Request a item for yourself.")
    @app_commands.guilds(discord.Object(id =GUILD_ID))
    async def request(self, interaction, *, item:str):
        await interaction.response.defer(thinking=True, ephemeral=True)
        member = interaction.user
        user = User(member.id)
        if str(user.id) not in open_json():
            await interaction.followup.send(
                "Unable to buy until you have linked your account."
            )
            return
        item = find_closest_item(item)
        can_buy = user.can_buy(item)
        view = RequestView(user, item, can_buy)
        embed = ItemEmbed(member, user, item)
        await interaction.followup.send(embed=embed, view=view)

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


async def setup(bot):
    await bot.add_cog(RequestCog(bot=bot))