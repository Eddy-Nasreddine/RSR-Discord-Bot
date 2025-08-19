import json
import os
from discord.ext import commands
from discord import app_commands
from constants import GUILD_ID, GUILD_ID, BOT_ADMINS_IDS
import discord
from helper import *


class AddCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="add", description="Will force link a user.")
    @app_commands.guilds(discord.Object(id =GUILD_ID))
    async def command(self, interaction, *, member:discord.Member, row:int):
        if interaction.user.id not in BOT_ADMINS_IDS:
            await interaction.response.send_message(
                "You do not have permission to use this command.",
                ephemeral=True
            )
            return
        user_id = member.id
        write_json(user_id, row)
        await interaction.response.send_message(f"User `{member.name}` is now linked to row `{row}`.")
            
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")
    
    
async def setup(bot):
    await bot.add_cog(AddCog(bot=bot))