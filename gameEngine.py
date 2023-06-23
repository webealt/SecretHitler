from utils import *

'''
functions
--> gameStream(message: message object, cmd: command string) ///This is the input from Bot_Comms to the engine

'''
async def gameStream(message, cmd):
    print("gameEngine recieved this command: " + cmd)
    
    if cmd == "load":
        await msgChan(message, "Starting Secret Hitler... \n type !join to join and !start to start")