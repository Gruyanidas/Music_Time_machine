from web_scraper import WebScraper
from spotify_handler import SpotifyHandler

def main():
	try:
		scraper = WebScraper()
		user_input = scraper.handle_input()
		scraper.scrape_data()
		#At this point scraper object has the list of all songs (top 100) for users desired year.
		top_100_hits = scraper.songs
		print(f"Scraped {len(top_100_hits)} songs from Billboard.")
		manager = SpotifyHandler()
		for song in top_100_hits:
			search_result = manager.search_for_song(song, year=user_input)
			if search_result:
				manager.handle_result(search_result)
		manager.validate_song_uris()
		#At this point we have all the found songs in collection under manager.songs_collection attribute
		#Creating spotify playlist with our 100 songs collection
		manager.create_playlist(year=user_input)
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	main()