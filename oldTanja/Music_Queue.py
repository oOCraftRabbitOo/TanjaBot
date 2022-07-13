import discord_commands
import Playlist_Music as pm
import time
import global_variables
import asyncio
import discord
import youtube_dl

index = 0   # Will be increased by 1 after first song has been played.
pm.create_new_playlist('Queue')

async def play_url(message, client, args):  # Plays a song from YouTube
    url = args[0]
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except youtube_dl.utils.DownloadError:
            info = ydl.extract_info("https://www.youtube.com/watch?v=0lhhrUuw2N8", download=False)
        URL = info['formats'][0]['url']
    voice_client = client.voice_clients[0]
    voice_client.play(discord.FFmpegPCMAudio(URL), after=lambda x=None: asyncio.run(after_life(message, client)))

async def after_life(message, client):
    global index
    index += 1
    index %= len(pm.all_playlists.get("Queue"))
    print(index)
    pm.load_all_playlists()
    queue = pm.all_playlists.get("Queue")
    await play_url(message, client, queue[index])

def increase_index(n):
    global index
    index += n
    index %= len(pm.all_playlists.get("Queue"))

async def skip(message, client, args):
    if len(args) >= 1:
        x = int(args[0])
    else:
        x = 1
    voice = discord.utils.get(client.voice_clients, guild=message.guild)
    if voice.is_playing():
        increase_index(x-1)
        voice.stop()
        await message.channel.send(f'{x} song(s) skipped')
    else:
        await message.channel.send("There is no audio playing right now.")

async def back(message, client, args):
    if len(args) >= 1:
        x = int(args[0])
    else:
        x = 1
    voice = discord.utils.get(client.voice_clients, guild=message.guild)
    if voice.is_playing():
        increase_index(-x-1)
        voice.stop()
        await message.channel.send(f'Went {x} song(s) back')
    else:
        await message.channel.send("There is no audio playing right now.")

async def restart(message, client, args):
    voice = discord.utils.get(client.voice_clients, guild=message.guild)
    if voice.is_playing():
        increase_index(-1)
        voice.stop()
        await message.channel.send(f'Restarted current song')
    else:
        await message.channel.send("There is no audio playing right now.")

async def stop(message, client, args):
    global index
    index = 0
    server = message.guild
    voice = discord.utils.get(client.voice_clients,guild=server)
    voice.stop()
    pm.delete_playlist('Queue')    # Clears Queue
    pm.create_new_playlist('Queue')
    pm.save_all_playlists()
    await message.channel.send("Bot stopped. Queue cleared.")




