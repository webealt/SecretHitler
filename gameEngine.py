from utils import *

'''
functions
--> gameStream(message: message object, cmd: command string) ///This is the input from Bot_Comms to the engine

'''
async def gameStream(message, cmd):
    print("gameEngine recieved this command: " + cmd)
    
    if cmd.split(":")[0] == "load":
        await msgChan(message, "Starting Secret Hitler... \ntype !join to join and !start to start")
    elif cmd.split(":")[0] == "join":
        await msgDm(message, "Hello Welcome to Secret Hitler! \nPlease provide a Nickname...")