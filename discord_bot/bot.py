import logging
import discord
from core import with_logging

@with_logging
async def send_message(message):
    await message.channel.send('Hello!')


def run_bot(token):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        logging.info('%s is now operational', client.user)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        logging.info('%s said %s in %s', username, user_message, channel)

        if user_message == '!hello':
            await send_message(message)
    client.run(token)
