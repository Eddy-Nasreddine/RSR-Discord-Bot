import discord
from discord.ext import commands
import asyncio
from constants import GUILD_ID, DISCORD_TOKEN, GUILD_ID

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix="$", intents=intents, help_command=None)
        
    async def setup_hook(self) -> None:
        self.tree.clear_commands(guild=discord.Object(id=GUILD_ID))
        await self.load_extension("commands.test")
        await self.load_extension("commands.Link")
        await self.load_extension("commands.Buy")
        await self.load_extension("commands.Attendance")
        await self.load_extension("commands.Add")
        await self.load_extension("commands.Refund")


        await self.tree.sync(guild=discord.Object(id=GUILD_ID))
        print("synced")
        
    async def on_command_error(self, ctx, error) -> None:
        await ctx.reply(error)
        
bot = Bot()

async def run():
    while bot.user.avatar.url is None:
        await asyncio.sleep(1)
        print("waiting...")
    
bot.run(DISCORD_TOKEN)
