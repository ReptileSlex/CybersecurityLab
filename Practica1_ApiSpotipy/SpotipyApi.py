import os
import sys
import json
import spotipy
import webbrowser
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyOAuth

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Error, el uso es: %s username" % (sys.argv[0],))
    sys.exit()
# Get the username from terminal
username = sys.argv[1]
# User ID: reptileslex

# Prompt for user permission

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth_manager=SpotifyOAuth())

user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user["display_name"]
followers = user["followers"]["total"]
print(">>>>> Bienvenido " + displayName + " a mi practica con APIs usando Spotify <<<<<")
print(">>>>> Tienes ", followers, "seguidores <<<<<")
while True:
    print()
    print("0 - Salir")
    print("1 - Buscar un artista")
    print("2 - Ver tus artistas más escuchados")
    print()
    choice = input("Tu selección es: ")

    if choice == "1":  # Busca al artista
        print()
        searchQuery = input("Excelente, ¿Cuál es su nombre?: ")
        print()

        # Obtiene los datos de la búsqueda
        searchResults = spotifyObject.search(searchQuery, 1, 0, "artist")
        print(json.dumps(searchResults, sort_keys=True, indent=4))
    elif choice == "2":
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-top-read"))
        topArtistsShortTerm = sp.current_user_top_artists(10, 0, "short_term")
        topArtistsMediumTerm = sp.current_user_top_artists(10, 0, "medium_term")
        topArtistsLongTerm = sp.current_user_top_artists(10, 0, "long_term")
        topartists = sp.current_user_top_artists(10, 0, "short_term")
        # print(json.dumps(topartists["items"][1], sort_keys=True, indent=4))
        # print("1", topartists["items"][1]["name"], " - Popularidad: ", topartists["items"][1]["popularity"])
        # print(len(topartists["items"]))

        print(">>>>>>>>>>>Top artistas escuchados el último mes<<<<<<<<<<<")
        for i in range(len(topArtistsShortTerm["items"])):
            print(i, topArtistsShortTerm["items"][i]["name"],
                  "\nPopularidad: ", topArtistsShortTerm["items"][i]["popularity"],
                  "-- Seguidores: ", topArtistsShortTerm["items"][i]["followers"]["total"],
                  "\n-- Género(s): ", topArtistsShortTerm["items"][i]["genres"][0:2])
            print()
        print()

        print(">>>>>>>>Top artistas escuchados los últimos 6 meses<<<<<<<<")
        for i in range(len(topArtistsMediumTerm["items"])):
            print(i, topArtistsMediumTerm["items"][i]["name"],
                  "\nPopularidad: ", topArtistsMediumTerm["items"][i]["popularity"],
                  "-- Seguidores: ", topArtistsMediumTerm["items"][i]["followers"]["total"],
                  "\n-- Género(s): ", topArtistsMediumTerm["items"][i]["genres"][0:2])
            print()
        print()

        print(">>>>>>>>>>>>Top artistas escuchados (All data)<<<<<<<<<<<<<")
        for i in range(len(topArtistsLongTerm["items"])):
            print(i, topArtistsLongTerm["items"][i]["name"],
                  "\nPopularidad: ", topArtistsLongTerm["items"][i]["popularity"],
                  "-- Seguidores: ", topArtistsLongTerm["items"][i]["followers"]["total"],
                  "\n-- Género(s): ", topArtistsLongTerm["items"][i]["genres"][0:2])
            print()
        print()

    # Finalizar programa
    elif choice == "0":
        break
