import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")

def test_connection():
    url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params = {'key': API_KEY, 'steamids': STEAM_ID}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        player = response.json()['response']['players'][0]
        print(f"✅ Connection Successful! Hello, {player['personaname']}")
    else:
        print(f"❌ Connection Failed. Status Code: {response.status_code}")

if __name__ == "__main__":
    test_connection()