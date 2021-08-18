import discord
import os
import requests
import json
from keep_alive import keep_alive
from discord.ext import commands, tasks

client = commands.Bot(command_prefix="?")

# @client.event
# async def on_member_join(member):
#   print(f'{member} has joined')

# @client.command()
# async def on_command_error(ctx,error):
#   if isinstance(error,commands.CommandNotFound):
#     await ctx.send("Command is not found")

# @client.event
# async def on_member_remove(member):
#   print(f'{member} has joined')

# @client.command()
# async def clear(ctx,amount = 5):
#   await ctx.channel.purge(limit = amount)

@client.command()
async def load(ctx,extension):
  await ctx.load_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx,extension):
  await ctx.unload_extension(f'cogs.{extension}')
  await ctx.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
  await ctx.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f'cogs.{filename[:-3]}')

# keep_alive()
client.run(os.environ['TOKEN'])  