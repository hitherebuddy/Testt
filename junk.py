import discord
from discord.ext import commands
import asyncio

#Prefix

bot = commands.Bot(command_prefix='!')

#Bot Status

@bot.event
async def on_ready():
  print("hello there!")
  print(bot.user.name)
  print(bot.user.id)
  
#Commands

@bot.command(pass_context = True)
async def lmao():
  await bot.say("ayy lmaoo")

@bot.command(pass_context = True)
async def info():
  await bot.say("Im Dumb Bot, a dumb bot.")
  
@bot.command(pass_context = True)
async def hello():
	await bot.say("Hi there")

#Token

bot.run('YEzh5B_yuc07aU-HqZZXYd81SZ2blZ-p')
