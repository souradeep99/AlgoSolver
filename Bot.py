import discord 
import os
from discord.ext import commands, tasks
from itertools import cycle

#TOKEN = 'NzI5MDE0MTY5Nzg0ODExNTkw.XwCyww.0-b6ZTqEQLOiwHna1BushZg8rQs'

#TOKEN = '1dUa_T_yJ25aCMCAPERuWlSm18pSanyE'
#NzI5MDE0MTY5Nzg0ODExNTkw.XwCxWg.lCLmKTJWrX1UektoZqoIHELJtgg

TOKEN = 'NzI5MDE0MTY5Nzg0ODExNTkw.XwCxWg.BshO5ofJvwVTz6Q9bp0OR0kWSJE'

client = commands.Bot(command_prefix = '.')

status = cycle(['Codeforces', 'CodeChef', 'AtCoder', 'HackerEarth', 'Hackerrank', 'CSES', 'A2OJ'])
players = {}



@client.event
async def on_ready():
    change_status.start()
    print('Bot is Online!')

@client.command()
async def clear(ctx, amount = 4):
    await ctx.channel.purge(limit = amount)

@client.command()
async def load(ctx, extension):
    client.load_extension('cogs.{}'.format(extension))

@client.command()
async def unload(ctx, extension):
    client.unload_extension('cogs.{}'.format(extension))

@client.command()
async def reload(ctx, extension):
    client.reload_extension('cogs.{}'.format(extension))


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')



@tasks.loop(seconds = 5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))


client.run(TOKEN)