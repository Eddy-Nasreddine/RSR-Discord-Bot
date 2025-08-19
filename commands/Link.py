import json
import os
from discord.ext import commands
from discord import app_commands
from constants import GUILD_ID, GUILD_ID
import discord
from helper import *


class LinkCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="link", description="This command links your Discord account to your row on the google sheet.")
    @app_commands.guilds(discord.Object(id =GUILD_ID))
    async def command(self, interaction, *, row:int):
        user_id = interaction.user.id
        if str(user_id) not in open_json():
            write_json(user_id, row)
            await interaction.response.send_message(f"User `{interaction.user}` is now linked to row `{row}`.")
        else:
            await interaction.response.send_message(f"User `{interaction.user}` has already been linked.")
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")
    
    
async def setup(bot):
    await bot.add_cog(LinkCog(bot=bot))