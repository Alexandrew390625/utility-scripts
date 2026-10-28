# Utility Scripts Collection

A collection of useful standalone Python and JavaScript utility scripts.

These scripts were written to solve real problems and may be helpful to others.

## Scripts

### Word & Text Tools
| Script | Description |
|--------|-------------|
| `word_checker.py` | Extracts words from a text file and checks them against a dictionary. Reports recognized vs unrecognized words. |

### Number Tools
| Script | Description |
|--------|-------------|
| `number_namer.py` | Names very large numbers using English -illion scale, SI prefixes, and plain English descriptions. Supports interactive mode and CLI. |

### Games
| Script | Description |
|--------|-------------|
| `brawl_stars_club_finder.py` | Searches for open, family-friendly Brawl Stars clubs with low trophy requirements (requires Brawl Stars API token). |
| `roblox_game_stats.py` | Fetches public stats and thumbnail for a Roblox game by Place ID. |
| `cookie_run_guild_tracker.py` | Tracks Cookie Run Kingdom guild officer / contribution data across seasons. |
| `scratch_list_range_extension.js` | Scratch 3.0 custom extension: "list items FROM to TO of LIST joined by SEP" block. |

### Minecraft
| Script | Description |
|--------|-------------|
| `minecraft_mca_reader.py` | Parses Minecraft region (`.mca`) files and lists blocks (uses `nbt` library). |
| `bytes_to_minecraft_world.py` | Converts any file's raw bytes into a Minecraft 1.12.2 world (each byte → block ID). No external dependencies. |

### Chess
| Script | Description |
|--------|-------------|
| `chess_pgn_analyzer.py` | Fast multi-core PGN analyzer. Generates statistics: openings, ELO ranges, win rates, most played events/players, etc. |

### System / Audio
| Script | Description |
|--------|-------------|
| `wifi_passwords.py` | Retrieves saved Wi-Fi passwords on Windows, macOS, and Linux (NetworkManager). Run with admin/root for best results. |
| `audio_loudness_analyzer.py` | Analyzes WAV audio loudness (dBFS) and peak levels. |

## Requirements

Most scripts only need the Python standard library.

Some require extra packages:

```bash
pip install requests nbt chess numpy
```

- `brawl_stars_club_finder.py` → `requests`
- `minecraft_mca_reader.py` → `nbt`
- `chess_pgn_analyzer.py` → `chess`
- `audio_loudness_analyzer.py` → `numpy`

## Usage Examples

```bash
# Number namer
python number_namer.py 1e27
python number_namer.py          # interactive

# Brawl Stars clubs (get token from https://developer.brawlstars.com)
python brawl_stars_club_finder.py --token YOUR_TOKEN

# Wi-Fi passwords
python wifi_passwords.py

# Chess PGN analysis
python chess_pgn_analyzer.py /path/to/pgns
```

## License

MIT License — free to use, modify, and share.

## Notes

- Some scripts contain hardcoded paths from the original environment (e.g. Android storage paths). Adjust them as needed.
- The Brawl Stars script requires your own API token and proper IP allowlisting on the developer portal.
- Use the Wi-Fi password script only on devices you own / have permission to access.
