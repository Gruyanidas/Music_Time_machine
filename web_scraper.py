from bs4 import BeautifulSoup
from datetime import datetime
import requests
import dotenv, os
import json
dotenv.load_dotenv()

class WebScraper:
	def __init__(self, date=None, songs:list[str]=None):

		self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/136.0"}
		self.date = date
		self.songs = songs

	@staticmethod
	def is_valid_date(date:str) -> bool:
		"""Checks for user input date and passes if it's correct"""
		try:
			datetime.strptime(date, '%Y-%m-%d')
			return True
		except ValueError:
			print("Entered date is not in a valid format! Please try again!")
			return False

	def handle_input(self) -> str:
		"""Handles user input"""
		while True:
			date = input("Which year do you want to travel to?"
					 " Enter date in a format YYYY-MM-DD such as 2023-03-21: ")
			if WebScraper.is_valid_date(date):
				self.date = date
				return self.date

	@staticmethod
	def perform_http_request(url: str, method: str = "GET", params=None, data=None, headers=None):
		"""Generic method to handle GET, POST, PUT"""
		try:
			method = method.upper()
			if method == "GET":
				response = requests.get(url=url, params=params, headers=headers, timeout=10)
			elif method == "POST":
				response = requests.post(url=url, json=data, headers=headers, timeout=10)
			elif method == "PUT":
				response = requests.put(url=url, json=data, headers=headers, timeout=10)
			elif method == "DELETE":
				response = requests.delete(url=url, headers=headers, timeout=10)
			else:
				raise ValueError(f"Unsupported HTTP method: {method}")

			response.raise_for_status()
			return response

		except requests.exceptions.Timeout:
			raise RuntimeError("Request timed out. Try again later.")
		except requests.exceptions.ConnectionError:
			raise RuntimeError("Network connection error. Check your internet.")
		except requests.exceptions.HTTPError as http_err:
			raise RuntimeError(f"HTTP error occurred for {method} {url}: {http_err}")
		except requests.exceptions.RequestException as req_err:
			raise RuntimeError(f"Request failed: {req_err}")
		except json.JSONDecodeError:
			raise RuntimeError("Failed to parse JSON response.")

	def scrape_data(self) -> list[str]:
		"""Scrapes web url and returns list of songs for requested date"""
		scraping_url = "https://www.billboard.com/charts/hot-100/" + self.date
		response = WebScraper.perform_http_request(url=scraping_url, method="GET", headers=self.header)
		web_page = response.text
		soup = BeautifulSoup(web_page, "lxml")
		song_names_spans = soup.select("li ul li h3")
		songs = [song.get_text().strip() for song in song_names_spans]
		self.songs = songs
		return self.songs