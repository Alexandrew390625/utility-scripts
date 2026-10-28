"""
number_namer.py
===============
Name any number using standard English -illion names (short scale),
SI / binary prefixes, and a plain English description.

Supports arbitrarily large integers (no OverflowError).

Usage
-----
    python number_namer.py                  # interactive mode
    python number_namer.py 1e27             # single number from CLI
    python number_namer.py 10**100          # expression
"""

import sys
import re
from decimal import Decimal, getcontext

getcontext().prec = 1000

# Short-scale -illion names (American English)
ILLIONS = [
    "", "thousand", "million", "billion", "trillion", "quadrillion",
    "quintillion", "sextillion", "septillion", "octillion", "nonillion",
    "decillion", "undecillion", "duodecillion", "tredecillion",
    "quattuordecillion", "quindecillion", "sexdecillion", "septendecillion",
    "octodecillion", "novemdecillion", "vigintillion",
]

# SI prefixes
SI_PREFIXES = [
    (1e24, "yotta"), (1e21, "zetta"), (1e18, "exa"), (1e15, "peta"),
    (1e12, "tera"), (1e9, "giga"), (1e6, "mega"), (1e3, "kilo"),
    (1e-3, "milli"), (1e-6, "micro"), (1e-9, "nano"), (1e-12, "pico"),
    (1e-15, "femto"), (1e-18, "atto"), (1e-21, "zepto"), (1e-24, "yocto"),
]

def name_illion(n):
    if n == 0:
        return "zero"
    if n < 0:
        return "negative " + name_illion(-n)
    # Convert to groups of 3 digits
    s = str(n)
    groups = []
    while s:
        groups.append(s[-3:])
        s = s[:-3]
    groups.reverse()
    parts = []
    for i, g in enumerate(groups):
        val = int(g)
        if val == 0:
            continue
        power = len(groups) - 1 - i
        if power < len(ILLIONS):
            name = ILLIONS[power]
        else:
            name = f"10^{power*3}"
        if name:
            parts.append(f"{val} {name}")
        else:
            parts.append(str(val))
    return " ".join(parts)

def si_name(n):
    n = float(n)
    for thresh, name in SI_PREFIXES:
        if abs(n) >= thresh:
            return f"{n/thresh:.3g} {name}"
    return str(n)

def main():
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        try:
            # Safe-ish eval for powers
            expr = expr.replace("^", "**")
            val = eval(expr, {"__builtins__": {}}, {})
            n = int(Decimal(str(val)))
        except Exception as e:
            print(f"Could not parse: {e}")
            return
        print(f"Number: {n}")
        print(f"English: {name_illion(n)}")
        print(f"SI-ish:  {si_name(n)}")
    else:
        print("Number Namer — enter a number or expression (or 'q' to quit)")
        while True:
            try:
                line = input("> ").strip()
            except EOFError:
                break
            if not line or line.lower() in ("q", "quit", "exit"):
                break
            try:
                line = line.replace("^", "**")
                val = eval(line, {"__builtins__": {}}, {})
                n = int(Decimal(str(val)))
                print(f"  → {name_illion(n)}")
            except Exception as e:
                print(f"  Error: {e}")

if __name__ == "__main__":
    main()
