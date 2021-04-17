import os, random, config
import discord
from discord.ext import commands, tasks

TOKEN = config.TOKEN

bot = commands.Bot(description="Bruno s2 André Forever!", command_prefix='s2', case_insensitive=True)
status = [
    'Forza Horizon',
    'Fumando',
    'Brunos2André',
    'Andrés2Bruno'
]

@bot.event
async def on_ready():
    print('I\'m in as {}'.format(bot.user))

@tasks.loop(seconds=30)
async def change_status():
  await bot.change_presence(activity=discord.Game(random.choice(status)))

# @bot.listen()
# async def on_message(message):
#     message.content = message.content.lower()
#     print(message.content)

@bot.command(name='andre', aliases=['André'], help="Expressa o quando o André ama o Bruno.")
async def andre(ctx):
    response = "André s2 Bruno"
    await ctx.send(response)

@bot.command(name='bruno', help="Expressa o quando o Bruno ama o André.")
async def bruno(ctx):
    response = "Bruno s2 André"
    await ctx.send(response)

@bot.command(name='play', help="Toca a playlist preferida do Bruno.")
async def play(ctx):
    response = "-play https://open.spotify.com/playlist/74vdw0pW7YbDEWAm3y3RHW?si=da8cc26c70b1471a"
    await ctx.send(response)

@bot.command(name='cade', help="Aonde está o Bruno?")
async def cade(ctx):
    responses = [
      "Estou na esquina!",
      "Tomando energético!",
      "Amando o s2 André s2",
      "Fui fumar.",
      "Já te respondo, meu Rwindows travou.",
      "Dando um apt-get"
    ]

    await ctx.send(random.choice(responses))

bot.run(TOKEN)