# These are descriptions of the commands
command_descriptions = {"help": "Displays this message",
            "ping": "Ping the server to see the latency",
            "join": "Joins a voice channel",
            "leave": "Leaves the voice channel",
            "play [song]": "Plays a song, either from the URL or the name",
            "play [playlist]": "Plays a playlist",
            "pause": "Pauses the current song",
            "resume": "Resumes the song again",
            "stop": "Stops the current song and clears the queue",
            "restart": "Restarts the current song from the beginning",
            "add_list [playlist]": "Creates a playlist, name may only be one word",
            "delete_list [playlist]": "Delete a playlist",
            "add [playlist] [song]": "Adds a song to a playlist",
            "remove [playlist] [song]": "Removes a song from a playlist",
            "lists": "Prints out all the playlists",
            "list [playlist]": "Shows the content of a playlist",
            "shuffle": "Shuffles the current queue",
            "prefix [new prefix]": "Changes the prefix of the bot",
            "top10": "See the Top 10 most common spelling mistakes"}


async def help_message(message, client, args):  # This sends a message containing command descriptions
    out = "> **The following commands are available:**\n> ‎\n"  # ‎ is an empty character
    for command in command_descriptions:
        out += f"> **{command}:**  {command_descriptions[command]}\n"
    await message.channel.send(out)
    """
    send_msg(out) could not be used, because of circular imports (discord_commands.py -> help.py -> discord_commands.py)
    A separate file for send_msg() would be better, but I didn't want to create a new file just for a single command.
    """
