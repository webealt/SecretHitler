# Declaratons
from gameEngine import gameStream
from dotenv import load_dotenv
from utils import *

load_dotenv()

server = server()
client = server.client

"""
Functions
--> command(message: message object, cmd: command string) /// This processes commands

"""


async def command(message, cmd):
    if message.channel.name == server.useChannel:
        print("BotComms recieved this command: " + cmd)

        if cmd == "hello":
            await msgChan(message, "Hi how are ya?")

        elif cmd == "dmTest":
            await msgDm(message, "Hello There")

        elif cmd == "loadTest":
            await gameStream(message, "load")


"""
Events
"""


@client.event
async def on_ready():
    guild_count = 0

    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    print("Secret Hitler Bot is in " + str(guild_count) + " guilds.")


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL and DMs.
@client.event
async def on_message(message):
    if not message.guild:
        return
    elif message.content[0] == "!":
        await command(message, message.content[1:])


# starts bot
client.run(server.DISCORD_TOKEN)
