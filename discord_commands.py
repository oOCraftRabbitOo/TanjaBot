import json
import ast

import discord

from global_variables import *
import Playlist_Music as pm
from Search_URL_in_Youtube import *
from help import *
from Music_Queue import *

async def changeprefix(message, client, args):
    if message.author.guild_permissions.administrator:
        server = message.guild
        global prefix
        prefix = args[0]
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(server.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)

        await send_msg(message, f"The prefix is changed to {prefix}")
    else:
        await send_msg(message, "Please ask an admin to change the prefix.")


def loadprefix():
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(server_id)]


def cmd_from_msg(event):
    prefix = loadprefix()
    no_prefix = event.content[len(prefix):]
    arguments = no_prefix.split(" ")
    command = arguments[0].lower()
    arguments.pop(0)
    return [command, arguments]


async def send_msg(message, string):  # Sends a message to the channel
    await message.channel.send(string)


async def unknown_command(message):  # Sends a message to the channel, if the command is unknown
    save_command(cmd_from_msg(message)[0])  # Saves misspellings to find alternative names. (e.g. "-p" for "-play")
    await send_msg(message, f"You wanted me to do '{cmd_from_msg(message)[0]}', but I didn't understand that.")


async def ping(message, client, args):  # Informs the user of the bot's latency
    await send_msg(message, f"My ping is {client.latency * 1000:.0f}ms.")


async def nothing(message, client, args):  # Does nothing...
    await send_msg(message, f"You wanted me to do 'nothing', but I'm restless.")


async def join(message, client, args):  # Joins a voice channel
    channel = message.author.voice.channel
    try:
        await channel.connect()
    except discord.ClientException:
        await send_msg(message, "I'm already in a voice channel.")


async def leave(message, client, args):  # Leaves a voice channel
    server = message.guild
    for x in client.voice_clients:
        if x.guild == server:
            return await x.disconnect()
    await send_msg(message, "I'm not in a voice channel.")


async def pause(message, client, args):
    server = message.guild
    voice = discord.utils.get(client.voice_clients,guild=server)
    if voice.is_playing():
        voice.pause()
    else:
        await send_msg(message, "There is no audio playing right now.")


async def resume(message, client, args):
    server = message.guild
    voice = discord.utils.get(client.voice_clients,guild=server)
    if voice.is_paused():
        voice.resume()
    else:
        await send_msg(message, "There is no audio paused right now.")


async def play_with_search(message, client, args):  # Plays a song from a YouTube search
    search_term = args[0]
    for i in args[1:]:
        search_term += " " + i
    print(search_term)
    await play_url(message, client, URL_Search_YT(args[0]))


async def play(message, client, args):  # Plays a song from YouTube
    voice = discord.utils.get(client.voice_clients, guild=message.guild)
    argument = args[0]
    for i in args[1:]:
        argument += " " + i
    if argument in pm.all_playlists.keys():
        await send_msg(message, pm.load_other_playlist(argument))
        if not voice.is_playing():
            await play_url(message, client, pm.all_playlists.get("Queue")[0])
    else:
        await add_song(message, client, ["Queue", argument])
    if not voice.is_playing():
        pm.load_all_playlists()
        if len(pm.all_playlists.get("Queue")) != 0:
            await play_url(message, client, pm.all_playlists.get("Queue")[0])

### Playlist commands ###

async def add_playlist(message, client, args):  # Creates a playlist
    name = args[0]
    output = pm.create_new_playlist(name)
    pm.save_all_playlists()
    await send_msg(message, output)


async def delete_playlist(message, client, args):  # Deletes a playlist
    name = args[0]
    if name != "Queue":
        output = pm.delete_playlist(name)
    else:
        pm.delete_playlist(name)
        pm.create_new_playlist("Queue")
        pm.add_song("Queue", "Never Gonna Give You Up")
        output = f'You sneaky little fella, you cannot delete the Queue. But I cleared it for you.'
    await send_msg(message, output)

async def add_song(message, client, args):  # Adds a song to a playlist
    name_playlist = args[0]
    name_song = args[1]
    for i in args[2:]:
        name_song += " " + i
    output = pm.add_song(name_playlist, name_song)
    pm.save_all_playlists()
    await send_msg(message, output)


async def remove_song(message, client, args):  # Deletes a song from a playlist
    print(args)
    name_playlist = args[0]
    name_song = args[1]
    for i in args[2:]:
        name_song += " " + i
    output = pm.remove_song(name_playlist, name_song)
    await send_msg(message, output)


async def list_all_playlists(message, client, args):  # Lists all playlists
    output = pm.list_all_playlists()
    await send_msg(message, output)


async def list_all_songs_of_playlist(message, client, args):  # Lists a playlist
    if len(args) > 0:
        name_playlist = args[0]
    else:
        name_playlist = "Queue"
    output = pm.list_all_songs_of_playlist(name_playlist)
    await send_msg(message, output)


async def shuffle_playlist(message, client, args):  # Shuffels a playlist
    if len(args) > 0:
        name_playlist = args[0]
    else:
        name_playlist = "Queue"
    output = pm.shuffle_playlist(name_playlist)
    await send_msg(message, output)


# Saving module:

def load_unknown_commands():
    with open("unknown_commands.json", "r") as f:
        commands = json.load(f)
    return commands

def save_command(name):
    unknown_commands = load_unknown_commands()
    if name in unknown_commands.keys():
        unknown_commands[name] += 1
    else:
        unknown_commands[name] = 1
    with open("unknown_commands.json", "w") as f:
        json.dump(unknown_commands, f)


async def unknown_commands(message, client, args):  # Gives out a list of the top 10 most common mistakes
    unknown_commands = load_unknown_commands()

    sorted_keys = sorted(unknown_commands, key=unknown_commands.get)
    sorted_keys.reverse()
    sorted_keys = sorted_keys[:10]

    text = "> **TOP 10 Most Common Spelling Mistakes**\n> ‎\n"  # ‎ is an empty character
    for n,i in enumerate(sorted_keys):
        text += f"> {n+1}. {i} ({unknown_commands[i]} times) \n"
    await send_msg(message, text)


commands = {}
saved_commands = {}

file = open('commands.txt', 'r')
contents = file.read()
saved_commands = ast.literal_eval(contents)
file.close()

for k,v in saved_commands.items():
    for command in v:
        commands[command] = eval(k)

