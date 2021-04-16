import os, random, config
from discord.ext import commands

TOKEN = config.TOKEN

bot = commands.Bot(command_prefix='s2')

@bot.event
async def on_ready():
    print('I\'m in as {}'.format(bot.user))

@bot.command(name='andre', help="Expressa o quando o André ama o Bruno.")
async def andre(ctx):
    response = "André s2 Bruno"
    await ctx.send(response)

@bot.command(name='bruno', help="Expressa o quando o Bruno ama o André.")
async def bruno(ctx):
    response = "Bruno s2 André"
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