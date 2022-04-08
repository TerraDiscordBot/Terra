import discord
from discord.ext import commands
import os


bot = commands.Bot(command_prefix="./", help_command = None)

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print("logged in!")

bot.run("abcdtoken")