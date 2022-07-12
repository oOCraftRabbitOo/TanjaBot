import discord
#from threading import Thread

from global_variables import *
from discord_commands import *
from Music_Queue import *
from Playlist_Music import *

@client.event
async def on_ready():
    print('I am connected!!')

@client.event
async def on_message(message):
    prefix = loadprefix()
    if message.author == client.user or not message.content.startswith(prefix):
        # Stops the bot from getting triggered by bots and ignores messages that aren't commands
        return

    try:
        load_all_playlists()
        await commands[cmd_from_msg(message)[0]](message, client, cmd_from_msg(message)[1])
        save_all_playlists()  # Saves the playlists to the file every time a command is run to prevent data loss
    except KeyError:
        await unknown_command(message)

client.run(token)

