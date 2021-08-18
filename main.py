import discord
import os
import requests
import json
from keep_alive import keep_alive
from discord.ext import commands, tasks

client = commands.Bot(command_prefix="?")

@client.command(aliases= ["l"])
async def load(ctx,extension):
  client.load_extension(f'cogs.{extension}')

@client.command(aliases= ["rel"])
async def reload(ctx,extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')

@client.command(aliases= ["ul"])
async def unload(ctx,extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
client.run(os.environ['TOKEN'])  