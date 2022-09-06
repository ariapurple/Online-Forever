import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
import threading

with open('tokens.txt') as my_file:
  tokens = my_file.readlines()

def onliner(token):
  client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

  @client.event
  async def on_ready():
      await client.change_presence(status=discord.Status.online)
      print(f'Logged in as {client.user} (ID: {client.user.id})')
  client.run(token)
  
threads = list()
for token in tokens:
  x = threading.Thread(target=onliner, args=(token,))
  threads.append(x)
  x.start()

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    # os.system('clear')
    print(f'Logged in as {client.user} (ID: {client.user.id})')
keep_alive()
client.run("Your main TOKEN")
