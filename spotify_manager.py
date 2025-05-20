import requests
from spotipy import Spotify
from typing import List


class SpotifyManager:

    def __init__(self, user_id: str, year, auth_sp: Spotify):
        self.user_id = user_id
        self.auth_sp = auth_sp
        self.song_uri_list = []
        self.year:str = year  ##Year range in str. e.g. "2001-2002"
        self.playlist_uri = ""

    def make_list_of_songs(self, song_names: List[str], track) -> None:
        for song in song_names: ## song_names: scrapped song list
            query = f"track:{song} year:{self.year}"
            result = self.auth_sp.search(q=query, limit=1, type="track")
            print("MAKE LIST OF SONGS RESULT: ", result)

            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uri_list.append(uri)
                print("SONG LIST URI: ", self.song_uri_list)
            except IndexError as e:
                print(f"Index Error: {song} doesn't exist in Spotify: {e}")

    def create_playlist(self, playlist_name):
        try:
            result = self.auth_sp.user_playlist_create(user=self.user_id, name=playlist_name)
            print(f"{playlist_name} has been created successfully")
            print("PLAYLIST DETAILS: ", result)
            self.playlist_uri = result["uri"].split(":")[2]
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
        except Exception as e:
            print(f"{playlist_name} has failed to be generated: {e}")

    def add_songs_into_playlist(self):
        print("PLAYLIST URI: ", self.playlist_uri)
        self.auth_sp.playlist_add_items(playlist_id=self.playlist_uri, position=0, items=self.song_uri_list)
