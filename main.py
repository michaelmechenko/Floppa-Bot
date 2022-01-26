import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print("User logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('floppa'):
        await message.channel.send('floppa')
    if message.content.startswith('?hi'):
        await message.channel.send('floppa says hello')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(
    name="floppa",
    description="floppa saying floppa",
    guild_ids=[374371380478607366])

async def _floppa(ctx:SlashContext):
    await ctx.send("floppa")

token = os.getenv('FLOPPATOKEN')
client.run(token)