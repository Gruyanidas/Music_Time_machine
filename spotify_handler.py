import spotipy
from spotipy.oauth2 import SpotifyOAuth
import dotenv, os
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException
import re
dotenv.load_dotenv()

class SpotifyHandler:

	SPOTIFY_ID = os.getenv("SPOTIFY_ID")
	SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
	API_SEARCH_ENDPOINT = os.getenv("API_SEARCH_ENDPOINT")
	REDIRECT_URL = os.getenv("REDIRECT_URL")
	SCOPE = "playlist-modify-public"

	def __init__(self, songs_collection:list[tuple]=None):
		self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
			client_id=self.SPOTIFY_ID,
			client_secret=self.SPOTIFY_SECRET,
			redirect_uri=self.REDIRECT_URL,
			scope=self.SCOPE
		))
		self.user_id = self.sp.current_user()['id']
		self.songs_collection = songs_collection if songs_collection is not None else []
		self.valid_song_uris = []

	def create_playlist(self, year:str):
		# Create a new playlist
		playlist_name = f"Best of the best from {year}"
		playlist_description = f"Timeless songs of {year}"
		playlist = self.sp.user_playlist_create(user=self.user_id, name=playlist_name, public=True,
										   description=playlist_description)
		playlist_id = playlist['id']
		print(f"Created playlist with ID: {playlist_id}")
		# List of track URIs you want to add (make sure these are valid Spotify track URIs)
		track_uris = [song_uri for song_uri, release_date in self.valid_song_uris]
		# Add tracks to the newly created playlist
		self.sp.playlist_add_items(playlist_id, track_uris)
		print("Tracks added successfully!")

	def search_for_song(self, song:str, year:str):
		params = {
			"q": f"{song}, {year}",
			"type": "track",
			"limit": 1,
		}
		result = self.sp.search(**params)
		return result

	def handle_result(self, result:dict) -> list:
		"""Takes search results from spotify and extracts data needed from json format"""
		try:
			song_uri = result["tracks"]['items'][0]['uri']
			song_release_date = result["tracks"]['items'][0]['album']['release_date']
		except (KeyError, ValueError):
			print("There is no data!")
		else:
			self.songs_collection.append((song_uri,song_release_date))


	def validate_song_uris(self) -> list[str]:
		"""	Validates a list of Spotify track URIs to ensure each is in the correct format.
		Expected format: 'spotify:track:' followed by exactly 22 alphanumeric characters."""
		# Define regex for a valid Spotify track URI
		pattern = re.compile(r"^spotify:track:[A-Za-z0-9]{22}$")
		for uri, date in self.songs_collection:
			if pattern.match(uri):
				self.valid_song_uris.append((uri, date))
			else:
				print(f"Skipping invalid URI: {uri}")
