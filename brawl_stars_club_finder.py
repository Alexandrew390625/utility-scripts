"""
Brawl Stars Club Finder
-----------------------
Searches for clubs that are:
  - Open (anyone can join)
  - Family friendly
  - Require <= 50,000 trophies

Usage:
  1. Get your API token from https://developer.brawlstars.com
  2. Run: python brawl_stars_club_finder.py --token YOUR_TOKEN_HERE
     Or set the env variable: BS_API_TOKEN=your_token python brawl_stars_club_finder.py
"""

import argparse
import os
import requests

BASE = "https://api.brawlstars.com/v1"

def get_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}

def search_clubs(token: str, name_query: str = "", limit: int = 200) -> list:
    url = f"{BASE}/clubs"
    params = {"name": name_query, "limit": limit} if name_query else {"limit": limit}
    resp = requests.get(url, headers=get_headers(token), params=params, timeout=10)
    if resp.status_code == 403:
        print("❌  Access denied. Check your API token and allowed IPs.")
        return []
    resp.raise_for_status()
    return resp.json().get("items", [])

def get_club_detail(token: str, club_tag: str) -> dict | None:
    tag = club_tag.replace("#", "%23")
    url = f"{BASE}/clubs/{tag}"
    resp = requests.get(url, headers=get_headers(token), timeout=10)
    if resp.status_code != 200:
        return None
    return resp.json()

def main():
    parser = argparse.ArgumentParser(description="Find open family-friendly Brawl Stars clubs")
    parser.add_argument("--token", default=os.getenv("BS_API_TOKEN"), help="Brawl Stars API token")
    parser.add_argument("--query", default="", help="Optional club name search")
    parser.add_argument("--limit", type=int, default=50, help="Max results")
    args = parser.parse_args()

    if not args.token:
        print("❌  No API token provided.\n"
              "    Use --token YOUR_TOKEN or set BS_API_TOKEN environment variable.\n"
              "    Get a token at: https://developer.brawlstars.com")
        return

    print("[*] Searching clubs...")
    clubs = search_clubs(args.token, name_query=args.query, limit=args.limit)
    print(f"[*] Found {len(clubs)} clubs (raw)")

    good = []
    for c in clubs:
        tag = c.get("tag", "")
        detail = get_club_detail(args.token, tag)
        if not detail:
            continue
        required = detail.get("requiredTrophies", 999999)
        type_ = detail.get("type", "")
        # open + low trophies
        if type_ == "open" and required <= 50000:
            good.append(detail)

    print(f"\n✅  {len(good)} clubs matching criteria (open + ≤50k trophies):\n")
    for d in good[:20]:
        print(f"  {d.get('name')}  {d.get('tag')}  trophies req: {d.get('requiredTrophies')}  members: {d.get('members', 0)}")
        print(f"     https://brawlify.com/stats/club/{d.get('tag','').replace('#','')}\n")

if __name__ == "__main__":
    main()
