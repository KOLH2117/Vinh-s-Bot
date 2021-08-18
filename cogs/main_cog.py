import discord
from discord.ext import commands

class main_cog(commands.Cog):
  def __init__(self, client):
      self.client = client
      self.help_message = """
```
General commands:
/help - displays all the available commands
/clear amount - will delete the past messages with the amount specified
Image commands:
/search <keywords> - will change the search to the keyword
/get - will get the image based on the current search
Music commands:
/p <keywords> - finds the song on youtube and plays it in your current channel
/q - displays the current music queue
/skip - skips the current song being played
```
"""
      self.text_channel_list = []

  #some debug info so that we know the bot has started    
  @commands.Cog.listener()
  async def on_ready(self):
    await self.client.change_presence(status= discord.Status.online,activity=discord.Game(name='?Help'))
    print("Ready")
  
@commands.Cog.listener()
async def on_member_join(member):
  print(f'{member} has joined')

@commands.command()
async def on_command_error(ctx,error):
  if isinstance(error,commands.CommandNotFound):
    await ctx.send("Command is not found")

@commands.Cog.listener()
async def on_member_remove(member):
  print(f'{member} has joined')

# @client.command()
# async def clear(ctx,amount = 5):
#   await ctx.channel.purge(limit = amount)

  # @commands.command(name="help", help="Displays all the available commands")
  # async def help(self, ctx):
  #   await ctx.send(self.help_message)

  # @commands.command(name="clear", help="Clears a specified amount of messages")
  # async def clear(self, ctx, arg):
  #   #extract the amount to clear
  #   amount = 5
  #   try:
  #       amount = int(arg)
  #   except Exception: pass

  #   await ctx.channel.purge(limit=amount)

def setup(client):
  client.add_cog(main_cog(client))