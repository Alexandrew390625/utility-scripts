# Utility Scripts Collection

A collection of useful standalone Python and JavaScript utility scripts.

This repository is also used to archive my projects.

These scripts were written to solve real problems and may be helpful to others.

## Scripts

| Script | Description |
|--------|-------------|
| `word_checker.py` | Extracts words from a text file and checks them against a dictionary. Reports recognized vs unrecognized words. |
| `number_namer.py` | Names very large numbers using English -illion scale, SI prefixes, and plain English descriptions. Supports interactive mode and CLI. |
| `brawl_stars_club_finder.py` | Searches for open, family-friendly Brawl Stars clubs with low trophy requirements (requires Brawl Stars API token). |
| `roblox_game_stats.py` | Fetches public stats and thumbnail for a Roblox game by Place ID. |
| `wifi_passwords.py` | Retrieves saved Wi-Fi passwords on Windows, macOS, and Linux (NetworkManager). Run with admin/root for best results. |
| `audio_loudness_analyzer.py` | Analyzes WAV audio loudness (dBFS) and peak levels. |
| `scratch_list_range_extension.js` | Scratch 3.0 custom extension: "list items FROM to TO of LIST joined by SEP" block. |
| `cookie_run_guild_tracker.py` | Tracks Cookie Run Kingdom guild officer / contribution data. |

## Archived Projects

The `archivedcoeds` folder contains archived code and projects.

## Requirements

Most scripts only need the Python standard library.

Some require extra packages:

```bash
pip install requests nbt chess numpy
```

## Usage Examples

```bash
# Number namer
python number_namer.py 1e27
python number_namer.py          # interactive

# Brawl Stars clubs (get token from https://developer.brawlstars.com)
python brawl_stars_club_finder.py --token YOUR_TOKEN

# Wi-Fi passwords
python wifi_passwords.py

# Audio
python audio_loudness_analyzer.py song.wav
```

## License

MIT License — free to use, modify, and share.

## Notes

- Some scripts contain hardcoded paths from the original environment (e.g. Android storage paths). Adjust them as needed.
- The Brawl Stars script requires your own API token and proper IP allowlisting on the developer portal.
- Use the Wi-Fi password script only on devices you own / have permission to access.

---

Want the full longer versions (chess PGN analyzer, Minecraft MCA readers, bytes-to-Minecraft world converter, more complete number namer, etc.)? Just tell me which ones and I will add them.
