import discord

with open('.token', 'r') as f:
    token = f.read()
client = discord.Client()
server_id = '961157523073802340'  # ID of the test server
voice_channel_id = '961157523073802344'  # ID of the test voice channe
