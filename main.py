from dotenv import load_dotenv
import os

from billboard_scraper import BillboardScraper
from spotify_auth import SpotifyAuth
from spotify_manager import SpotifyManager

load_dotenv()

spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_secret = os.getenv("SPOTIFY_SECRET")
spotify_redirected_uri = os.getenv("SPOTIFY_REDIRECTED_URI")
spotify_scope = os.getenv("SPOTIFY_SCOPE")


#=================================ASK THE TIME RANGE / PROCESS WEB SCRAPING============================================#

date_input = input(
    "Which year do you want to music-travel back to? Type the date in this format YYYY-MM-DD: "
)

billboard = BillboardScraper(date_input)
scraped_song_list = billboard.scrap_billboard()



#============================================SPOTIFY AUTHORIZATION===================================================#

spotify_auth = SpotifyAuth(
    client_id=spotify_client_id,
    client_secret=spotify_secret,
    redirected_uri=spotify_redirected_uri,
    scope=spotify_scope
)

prev_year = str(int(date_input.split("-")[0]) - 1)
current_year = date_input.split("-")[0]
spotify_id = spotify_auth.get_user_id()
playlist_name = f"{date_input}: Billboard 100"


#===================================CREATE A PLAYLIST AND ADD SONGS INTO IT=============================================#

spotify_manager = SpotifyManager(user_id=spotify_id, auth_sp=spotify_auth.sp, year=f"{prev_year}-{current_year}")
spotify_manager.make_list_of_songs(scraped_song_list, track="track")
# print("SONG URI LIST: ", spotify_manager.song_uri_list)
spotify_manager.create_playlist(playlist_name=playlist_name)
spotify_manager.add_songs_into_playlist()


