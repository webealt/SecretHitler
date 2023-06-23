import discord

import os
from dotenv import load_dotenv

'''
Classes
'''
class server():
	
    def __init__(self):
        intents = discord.Intents.all()
        self.client = discord.Client(intents=intents)
        self.useChannel = "bot-testing" # <-- Channel to point the bot too
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        

'''
Functions
--> msgChan(message: message object, text: text to send) /// Send message to channel using their message in channel as user reference
--> msgDm(message: message object, text: text to send) /// Dm user using their message in channel as user reference
'''
async def msgChan(message, text):
	await message.channel.send(text)

async def msgDm(message, text):
	user = server.client.get_user(message.author.id)
	await user.send(text)