# Projektbeschreibung

Bot, der in einem Sprachkanal auf Discord Audio von YouTube streamen kann. 
Zusätzlich kann der Bot Playlists erstellen und diese anpassen. Er wird per Text in einem Discord-Server gesteuert und kommuniziert über diesen mit dem User.


# Bedienungshinweise

Um den Bot zu starten muss nur main.py ausgeführt werden. Nun können im Test-Server folgende Commands benutzt werden. Mit -help kann eine ähnliche Liste direkt auf Discord angezeigt werden.


	-pause                      Pausiert die Audio-Wiedergabe.
	-resume                     Spielt Audio wieder von derselben Stelle ab, wie pausiert wurde.
	-ping                       Gibt Latenz zurück.  
	-join                       Bot joint in voice channel.  
	-leave                      Verlässt den voice channel.  

	-play [song]                Fügt Audio der Queue hinzu (egal ob URL oder Name). Falls nur der Name eingegeben wird, wird dieser auf YouTube gesucht und dann hinzugefügt.
	-play [playlist]	    Macht das selbe, nur mit einer erstellten Playlist.	
	-add_list [name]            Erstellt Playlist unter diesem Namen (nur ein Wort für den Namen)
	-delete_list [name]         Löscht Playlist mit diesem Namen  
	-lists                      Gibt Namen aller Playlists mit Anzahl Songs/Audios zurück  

	-add [playlist] [song]      Fügt Audio der vorgegebenen Playlist hinzu.  
	-remove [playlist] [song]   Entfernt Audio aus der vorgegebenen Playlist. 
	-list [playlist]            Gibt alle Namen der Audios der Playlist zusammen mit der Länge zurück.  
	-shuffle                    Mischt entweder die Queue.
	-stop   		    Löscht Queue, beendet Musikspielen
	-back ([n])  	            Springt zum letzten Song aus der Queue zurück. (Optional können mehrere Songs zurückgesprungen werden.)
	-skip ([n])      	    Überspringt den laufenden Song und spielt den nächsten Song aus der Queue. (Optional können mehrere Songs übergesprungen werden)  
	-restart    		    Audio beginnt von vorne 
	-prefix [new prefix]  	    Ändert Prefix (also "-" zum ) 
	-help   		    Gibt alle Funktionen mit Erklärungen zurück (ähnlich diesem Fenster)
	-top10			    Gibt die zehn häufigsten Tippfehler zurück, um alternative Schreibweisen hinzuzufügen. Dies soll das Benutzen des Bots angenehmer gestallten.



# Quellenverzeichnis

Library zum Interagieren mit Discord: [discord.py](https://discordpy.readthedocs.io/en/stable/api.html)


# Projektstand bei Zwischenabgabe

- [x] Discord Bot funktioniert
- [x] Bot kann in den Chat schreiben
- [x] Discord Bot kann Voice-Channels beitreten und verlassen
- [x] Bot kann Musik abspielen
- [ ] Bot kann YouTube-Suchen starten (teilweise implementiert)
- [ ] YouTube-Suche vollständig implementieren


# Projektstand bei Endabgabe

- [x] Discord Bot funktioniert
- [x] Bot kann in den Chat schreiben
- [x] Discord Bot kann Voice-Channels beitreten und verlassen
- [x] Bot kann Musik abspielen
- [x] Bot kann YouTube-Suchen starten (teilweise implementiert)
- [x] YouTube-Suche vollständig implementiert
- [x] Logging von Tippfehlern
- [x] Einfaches Hinzufügen von alternativen Command-Schreibweisen
- [x] Angenehmes -help "Fenster" innerhalb von Discord
