import json

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild)]
client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "-"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

@client.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = prefix

    with open ("prefixes.json", "w") as f:
        json.dump(prefixes,f)
    await ctx.send(f"The prefix is changed to {prefix}")

@client.event
async def on_message(msg):
    try:
        if msg.mentions[0] == client.user:
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

                pre = prefixes[str(msg.guild.id)] = prefix

            await msg.channel.send(f"My prefix for this server is {pre}")
    except:
        pass

    await client.process_commands(msg)
    
@client.command(pass_context=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("There is no audio playing right now.")

@client.command(pass_context=True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("There is no audio paused right now.")

@client.command(pass_context=True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.stop()

@client.command(pass_context=True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg)
    player = voice.play(source)
