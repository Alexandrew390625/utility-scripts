"""
Roblox Game Stats Checker
Fetches public stats for a Roblox game using the Roblox API.
"""

import requests

PLACE_ID = 4943297844          # change this to the Place ID you want
UNIVERSE_API = "https://games.roblox.com/v1/games"
THUMBNAIL_API = "https://thumbnails.roblox.com/v1/games/icons"

def main():
    # Get universe id from place id
    r = requests.get(f"https://apis.roblox.com/universes/v1/places/{PLACE_ID}/universe", timeout=10)
    r.raise_for_status()
    universe_id = r.json()["universeId"]
    print(f"Universe ID: {universe_id}")

    # Game details
    r = requests.get(UNIVERSE_API, params={"universeIds": universe_id}, timeout=10)
    r.raise_for_status()
    data = r.json()["data"][0]
    print(f"Name        : {data.get('name')}")
    print(f"Playing     : {data.get('playing'):,}")
    print(f"Visits      : {data.get('visits'):,}")
    print(f"Favorites   : {data.get('favoritedCount'):,}")
    print(f"Max Players : {data.get('maxPlayers')}")
    print(f"Created     : {data.get('created')}")
    print(f"Updated     : {data.get('updated')}")

    # Thumbnail
    r = requests.get(THUMBNAIL_API, params={
        "universeIds": universe_id,
        "size": "512x512",
        "format": "Png",
        "isCircular": "false"
    }, timeout=10)
    if r.ok:
        items = r.json().get("data", [])
        if items:
            print(f"Thumbnail   : {items[0].get('imageUrl')}")

if __name__ == "__main__":
    main()
