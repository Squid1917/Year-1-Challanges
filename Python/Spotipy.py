import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
from PIL import Image, ImageTk

# Set up Spotipy with your Spotify API credentials
client_id = "487fcb00b16a41d1802aee927ffdf8e1"  # Replace with your actual client ID
client_secret = "eee2edf54d2b428fb34417923cac7439"  # Replace with your actual client secret
redirect_uri = "https://localhost:8888/callback"  # Replace with your actual redirect URI
scope = "playlist-read-private user-library-read"  # Add any additional scopes as needed

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Fetch the saved tracks
limit = 50
offset = 0
all_tracks = []

while True:
    # Fetch tracks for the current offset
    results = sp.current_user_saved_tracks(limit=limit, offset=offset)
    items = results['items']

    # If no more items, break the loop
    if not items:
        break

    # Extract track information
    for idx, item in enumerate(items):
        track = item['track']
        song_name = track['name']
        artist = track['artists'][0]['name']  # Assume we only consider the first artist

        # Get the cover image URL if available
        if len(track['album']['images']) > 0:
            cover_image_url = track['album']['images'][0]['url']
        else:
            cover_image_url = "No cover image available"

        all_tracks.append(f"{idx + offset + 1}: {song_name} - {artist}\nCover Image: {cover_image_url}")

    # Increment the offset for the next request
    offset += limit

# Print all tracks with cover image URL in the desired format
# print("Your Songs:")
# for track_info in all_tracks:
#     print(track_info)

def displaySong(track_info_l , track_info_r):




def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if displaySong(left[i], right[j]):
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

mergeSort(all_tracks)
print(myList)