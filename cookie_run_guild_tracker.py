import json
import os
from datetime import datetime

DATA_PATH = "/storage/emulated/0/download/guild_data.json"
LEADER = "AndreiSmek"
START_SEASON = 29
START_PART = 1
PARTS_PER_SEASON = 4

def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return {"seasons": {}, "officers": {}}

def save_data(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

def main():
    data = load_data()
    print("Cookie Run Kingdom Guild Tracker")
    print(f"Leader: {LEADER}")
    print("Commands: add, list, summary, quit")
    # Simplified interactive for sharing. Original had more season tracking logic.
    while True:
        cmd = input("> ").strip().lower()
        if cmd in ("q", "quit", "exit"):
            break
        elif cmd == "list":
            print(json.dumps(data, indent=2))
        elif cmd.startswith("add"):
            print("Add contribution logic here (original tracked officers across seasons)")
        else:
            print("Unknown command")
    save_data(data)

if __name__ == "__main__":
    main()
