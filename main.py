import os, sys
import discord
from discord.ext.commands import Bot

try:
    TOKEN = os.environ['TOM_BOT_TOKEN']
except KeyError:
    print("ERROR: Please add an OAuth2 token to an environment variable 'TOM_BOT_TOKEN'.")
    sys.exit(1)

client = Bot(command_prefix="!")

@client.command(
    name='hello',
    description='Greets you.'
)
async def hello(context):
    await client.say("Hello, " + context.message.author.mention)

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name + "(" + client.user.id + ")")

client.run(TOKEN)
