import json

with open("music.json") as file:
    music = json.load(file)

user_input = input("Add an (artist/album/song): ")

while user_input != 'exit':
    if user_input == 'artist':
        artist = input("Which artist? ")
        if artist in music:
            print("Artist exists")
        else:
            music[artist] = {}
    elif user_input == 'album':
        artist = input("Which artist? ")
        if artist in music:
            album = input("Which album? ")
            if album in music[artist]:
                print("Album already exists :(")
            else:
                music[artist][album]={
                    'songs': [],
                    'year': int(input(f"When was {album} released? ")),
                    'platinum': True if input(f"Did {album} go platinum? (Y/N)").lower() == 'y' else False
                }
        else:
            print("Artist not found.")
    elif user_input == 'song':
        artist = input("Which artist? ")
        if artist in music:
            album = input("Which album? ")
            if album in music[artist]:
                song = input("Which song? ")
                if song in music[artist][album]['songs']:
                    print("Song already exists :(")
                else:
                    music[artist][album]['songs'].append(song)
    
    user_input = input("Add an (artist/album/song): ")

#print out the albums
for artist, albums in music.items():
    print(artist)
    for album, album_info in albums.items():
        print(" ", album)
        print("    Year published: ", album_info['year'])
        if album_info['platinum']:
            print("    This album went platinum")
        else:
            print("    BOoooo")
        for song in album_info['songs']:
            print("      ", song)
        print()
