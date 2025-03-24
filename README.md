🎶✨ MUSIC TIME MACHINE ⏳🚀
Travel through sound. Code through time.

Welcome to Music Time Machine – a fun, interactive Python project that lets you travel through musical history! 🚀
This app scrapes Billboard's Top 100 hits for a specific date, finds those songs on Spotify, and creates a personalized playlist just for you.
A perfect blend of 🎼 web scraping, 🎧 Spotify integration, and 💻 object-oriented programming.

Whether you're feeling nostalgic or just curious about the music from a particular era, this tool helps you rediscover classics and hidden gems – all while improving your Python skills.
🌟 Features at a Glance

    📅 Enter any date in history and instantly see the Billboard Top 100 from that day.

    🤖 Let the app build a Spotify playlist with those hits – automatically!

    🧱 Built using clean, modular, object-oriented Python code.

    💡 Easy to expand with new features like GUIs, analytics, or social sharing.

🧰 Tech Stack Highlights
🔧 Tool	💬 Purpose
🐍 Python	The core language driving the project
🍲 BeautifulSoup	Parses and scrapes the Billboard site
🌐 Requests	Handles HTTP requests
🎧 Spotipy	Talks to Spotify’s Web API
🔐 dotenv	Manages your secrets securely
🧩 OOP Architecture	Keeps everything clean and expandable

⚙️ Installation & Setup

Follow these simple steps to get Music Time Machine up and running:
📥 Clone the Repository

git clone https://github.com/Gruyanidas/Music_Time_machine.git
cd music-time-machine

🛡️ (Optional) Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

📦 Install Dependencies

pip install -r requirements.txt

🔐 Set Up Environment Variables

Create a .env file in the root directory and add your Spotify credentials:

SPOTIFY_ID=your_spotify_client_id
SPOTIFY_SECRET=your_spotify_client_secret
REDIRECT_URL=your_spotify_redirect_url

    💡 Make sure the redirect URL is registered in your Spotify Developer Dashboard.

▶️ Running the Program

Launch the app with:

python main.py

You'll be prompted to:

    📅 Enter a date (YYYY-MM-DD)

    🎼 Scrape Billboard’s Top 100 for that date

    🔎 Search for each song on Spotify

    📻 Automatically generate a playlist with your time-travel hits

🧠 How It Works

Here’s a breakdown of the key components that make the Music Time Machine tick:
🔍 Web Scraping – WebScraper Class

🧭 Navigates to Billboard’s Hot 100 page for the provided date
🗓️ Validates input date format (YYYY-MM-DD)
📄 Parses the HTML using BeautifulSoup
🎶 Extracts the top 100 song titles and artists
🎧 Spotify Integration – SpotifyHandler Class

🔍 Searches for each Billboard song on Spotify using the Spotipy library
✅ Validates each track’s URI
📂 Creates a brand new playlist in your Spotify account
🎵 Adds the found tracks directly into your playlist
🧱 Modular Architecture – OOP Design

🧩 Follows object-oriented principles for easy scaling
🔄 Each component is encapsulated and reusable
🚀 Enables quick feature additions like GUI, new music sources, or analytics


🚀 Expanding the Project

Music Time Machine is designed with scalability in mind. Here are a few exciting ideas to level it up:

    🌍 More Music Sources
    Add charts from other countries or platforms (e.g., UK Top 40, Apple Music, YouTube Trends).

    🖼️ Graphical User Interface (GUI)
    Build a desktop or web UI using tools like Tkinter, PyQt, or Flask.

    📝 Custom Playlist Features
    Let users choose playlist names, add descriptions, or select specific genres.

    📊 Music Analytics
    Display genre breakdowns, artist stats, or popularity scores for your playlist.

    📣 Social & API Integration
    Share playlists via Twitter or Instagram, or connect to more music APIs.

🤝 Contributing

I’d love your help! 🎉

    Fork the repository

    Create a new branch (git checkout -b feature-idea)

    Make your changes

    Push to your branch (git push origin feature-idea)

    Open a pull request

    🗣️ For major changes, please open an issue first to discuss your ideas.

📄 License

This project is licensed under the MIT License – feel free to use, modify, and share it.
🎤 Final Thoughts

Music Time Machine is more than just a project – it’s a nostalgic adventure through music history, powered by Python and the web. Whether you’re a developer, a music lover, or both, this app is a fun and educational way to explore the past.

Enjoy your journey through time – and happy coding! 🎶💻✨

❤️ Made with Love

Made with ❤️ by Milos Grujic (aka Gruyanidas)
Connect with me on LinkedIn or check out more of my work on GitHub!

    "I will unsheathe my sword by creating the code in my name!"