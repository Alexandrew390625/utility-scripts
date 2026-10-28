"""
word_checker.py
---------------
Reads a target file, extracts every word from it, and checks each word
against a dictionary. Prints a summary of recognized vs. unrecognized words.

Dictionary path: /storage/emulated/0/download/words.txt
"""

import re
import sys
import os

def load_dictionary(path):
    words = set()
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                w = line.strip().lower()
                if w:
                    words.add(w)
    except FileNotFoundError:
        print(f"[!] Dictionary not found: {path}")
        sys.exit(1)
    return words

def extract_words(text):
    return re.findall(r"[a-zA-Z']+", text)

def main():
    dict_path = "/storage/emulated/0/download/words.txt"
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Path to file to check: ").strip()

    if not os.path.isfile(target):
        print(f"[!] File not found: {target}")
        sys.exit(1)

    dictionary = load_dictionary(dict_path)
    print(f"[✓] Loaded {len(dictionary):,} dictionary words")

    with open(target, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    words = extract_words(text)
    total = len(words)
    unique = set(w.lower() for w in words)
    recognized = [w for w in unique if w.lower() in dictionary]
    unrecognized = [w for w in unique if w.lower() not in dictionary]

    print()
    print("─" * 60)
    print(f"  WORD CHECK REPORT — {os.path.basename(target)}")
    print("─" * 60)
    print(f"  Total word tokens   : {total:,}")
    print(f"  Unique words        : {len(unique):,}")
    print(f"  Recognized          : {len(recognized):,}  ({100*len(recognized)/max(1,len(unique)):.1f}%)")
    print(f"  Unrecognized        : {len(unrecognized):,}  ({100*len(unrecognized)/max(1,len(unique)):.1f}%)")
    print("─" * 60)

    if unrecognized:
        print("\n  ❌ Words NOT found in dictionary:\n")
        for w in sorted(unrecognized, key=str.lower):
            print(f"  {w}")
    else:
        print("\n  ✅ All unique words were found in the dictionary!")

if __name__ == "__main__":
    main()
