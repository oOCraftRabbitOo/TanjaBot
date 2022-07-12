import ast
import random

from Search_URL_in_Youtube import *
from global_variables import server_id



all_playlists = {}


def save_all_playlists(): #Speichert alle Playlists in eine Datei
    with open('Playlists.txt', 'w') as data:
        data.write(str(all_playlists))

def load_all_playlists(): #Lädt alle Playlists aus der Datei
    global all_playlists
    file = open('Playlists.txt', 'r')
    contents = file.read()
    all_playlists = ast.literal_eval(contents)
    file.close()

def create_new_playlist(name_playlist): #erstellt eine neue Playlist
    if name_playlist not in all_playlists.keys():
        all_playlists[name_playlist] = []
        return f'playlist {name_playlist} created'
    return f'playlist {name_playlist} already exists'

def delete_playlist(name_playlist): #Löscht eine Playlist
    if name_playlist in all_playlists.keys():
        all_playlists.pop(name_playlist)
        return f'playlist {name_playlist} deleted'
    return f'playlist {name_playlist} not found'


def add_song(name_playlist,name_song): #Fügt einen Song zu der Ausgewählten playlist hinzu
    search_result = URL_Search_YT(name_song)
    if name_playlist in all_playlists.keys():
        if search_result[1] not in list_all_songs_of_playlist(name_playlist):
            song_list = all_playlists.get(name_playlist)
            song_list.append(search_result)
            all_playlists.update({name_playlist: song_list})
            save_all_playlists()
            return f'{search_result[1]} added to playlist {name_playlist}'
        return f'song {search_result[1]} already in playlist {name_playlist} included'
    return f'playlist {name_playlist} not found'

def remove_song(name_playlist,name_song): #Entfernt einen Song aus der angefragten playlist
    if name_playlist in all_playlists.keys():
        song_list = all_playlists.get(name_playlist)
        for i in range(len(song_list)):
            if song_list[i][1] == name_song:
                song_list.pop(i)
                all_playlists.update({name_playlist: song_list})
                return f'song {name_song} removed from playlist {name_playlist}'
        return f'song {name_song} not found in playlist {name_playlist}'
    return f'playlist {name_playlist} not found'

def list_all_playlists(): #Gibt alle Playlists und deren Längen in einer Liste zurück
    output_list = [f'> **Here are all available playlists:**', "> ‎"]
    for n,(k,v) in enumerate(all_playlists.items()):
        output_list.append(f'> {n+1}. {k} ({len(v)})')
    return '\n'.join(output_list)

def list_all_songs_of_playlist(name_playlist): #Gibt eine liste aller Song_Namen der angefragten playlist zurück
    if name_playlist in all_playlists.keys():
        output_list = [f'> **Playlist "{name_playlist}" contains the following songs:**', "> ‎"]
        for k,v in all_playlists.items():
            if k == name_playlist:
                for n,name in enumerate(v):
                    output_list.append(f'> {n+1}. {name[1]}  **{name[2]}**')
        return '\n'.join(output_list)
    return f'playlist {name_playlist} not found'

def shuffle_playlist(name_playlist): #Shuffelt die angefragte playlist
    if name_playlist in all_playlists.keys():
        song_list = all_playlists.get(name_playlist)
        random.shuffle(song_list)
        all_playlists.update({name_playlist: song_list})
        return f'Shaken, not stirred'
    return f'playlist {name_playlist} not found'

def load_other_playlist(name_playlist):
    if name_playlist in all_playlists.keys():
        for song in all_playlists[name_playlist]:
            song_list = all_playlists.get('Queue')
            song_list.append(song)
        all_playlists.update({'Queue': song_list})
        save_all_playlists()
        return f'{name_playlist} added to Queue'
    return f'playlist {name_playlist} not found'