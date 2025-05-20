import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyAuth:
    def __init__(self, client_id, client_secret, redirected_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirected_uri = redirected_uri
        self.scope = scope
        self.sp = spotipy.Spotify(
                    auth_manager=SpotifyOAuth(
                        scope=self.scope,
                        redirect_uri=self.redirected_uri,
                        client_id=self.client_id,
                        client_secret=self.client_secret,
                        show_dialog=True,
                        cache_path="token.txt",
                    )
              )

    def get_user_id(self):
        print("CURRENT USER: ", self.sp.current_user())
        return self.sp.current_user()["id"]

