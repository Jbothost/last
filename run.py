#discord bot made by spud
#spud - youtube
#@Spud1425 - discord

##IMPORTS## 
import discord						#MAKE SURE YOU DO "py -m pip install discord" IN COMMAND PROMPT!
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time

##PREFIX##
bot = commands.Bot(command_prefix='!')

##BOT IS READY## 
@bot.event
async def on_ready():
    print("Bot Is Online! And Ready To Spam")
 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    while True:
        await bot.say("Oh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\n")
        await bot.say("Oh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\n")
        await bot.say("Oh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\n")
        await bot.say("Oh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\n")
        await bot.say("Oh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\nOh u just got pranked!\n")

##BOT TOKEN##
bot.run ("NDg5NDYyODkxNjI4NzI0MjM2.Dn7Tng.z3ydfUVVMne6RNZxpuJC4xv6NU8")
