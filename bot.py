import discord
from discord.ext import commands
from sys import argv
from .main import LaylaAI



layla: LaylaAI = LaylaAI()


TOKEN: str = argv[1]
BOT = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@BOT.event
async def on_ready() -> None:
    print(f"Logged in as {BOT.user.name}")

async def on_message(message: discord.Message) -> None:
    if message.author == BOT.user:
        return

    if message.content.channel.id == argv[2]:
        prompt = message.content
        response = layla.process_message(prompt, message.author.name)
        await message.channel.send(response)

BOT.run(TOKEN)
