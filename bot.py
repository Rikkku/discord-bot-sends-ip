import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True # Enable the members intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def whatip(ctx):
    # Open the file and read the text
    with open('ip.txt', 'r') as file:
        text = file.read()
        
    # Send the text to the channel
    await ctx.send(text)

# Replace YOUR_BOT_TOKEN with your bot token
bot.run('PLACE YOUR TOKEN HERE')
