import discord
from discord.ext import commands
from sys import argv


TOKEN: str = argv[1]
BOT = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@BOT.event
async def on_ready() -> None:
    print(f"Logged in as {BOT.user.name}")



BOT.run(TOKEN)