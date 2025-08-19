from discord.ext import commands
from discord import app_commands
from constants import GUILD_ID, GUILD_ID
import discord


class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="test", description="this is a test!")
    @app_commands.guilds(discord.Object(id =GUILD_ID))
    async def command(self, interaction):
        await interaction.response.send_message("This is a test message!")
        
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")
    
    
async def setup(bot):
    await bot.add_cog(TestCog(bot=bot))