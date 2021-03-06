import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext, cog_ext

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print("User logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('send me a picture floppa'):
        await message.channel.send(file=discord.File(r'C:\Users\Michael\Desktop\Discord Bots\Floppa Bot\imgs\floppa.jpg'))
    if message.content.startswith('hi floppa'):
        await message.channel.send('hi {0.author}'.format(message))
        return
    for word in message.content.split():
        if word == "floppa":
            await message.channel.send('floppa?')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="hello :)")
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="hello there")
        await ctx.send(content="test", embeds=[embed])

def setup(bot):
    bot.add_cog(Slash(bot))

@slash.slash(
    name="floppa",
    description="floppa")

async def _floppa(ctx:SlashContext):
    embed_text = discord.Embed(title="floppa", description="floppin'", color=0x00ff00)
    await ctx.channel.send(file=discord.File(r'C:\Users\Michael\Desktop\Discord Bots\Floppa Bot\imgs\floppa.jpg'), embed=embed_text)


token = os.getenv('FLOPPATOKEN')
client.run(token)
#bot.run(token)