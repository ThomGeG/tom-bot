import os
import discord

TOKEN = os.environ['TOM_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name + "(" + client.user.id + ")")

client.run(TOKEN)
