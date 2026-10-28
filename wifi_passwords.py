#!/usr/bin/env python3
"""
wifi_passwords.py - Check saved Wi-Fi passwords on your device.

Supports: Windows, macOS, Linux (NetworkManager)
Run with admin/root privileges for best results.
"""

import subprocess
import platform
import sys
import re

def get_wifi_passwords_windows():
    results = []
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "profiles"], text=True, errors="ignore")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error listing profiles: {e}")
        return results
    profiles = re.findall(r"All User Profile\s*:\s*(.+)", output)
    for profile in profiles:
        profile = profile.strip()
        try:
            detail = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"], text=True, errors="ignore")
            match = re.search(r"Key Content\s*:\s*(.+)", detail)
            password = match.group(1).strip() if match else "(no password / open network)"
        except subprocess.CalledProcessError:
            password = "(could not retrieve)"
        results.append({"ssid": profile, "password": password})
    return results

def get_wifi_passwords_macos():
    results = []
    try:
        preferred = subprocess.check_output(["networksetup", "-listpreferredwirelessnetworks", "en0"], text=True, errors="ignore")
        ssids = [line.strip() for line in preferred.splitlines() if line.strip() and "Preferred" not in line]
    except subprocess.CalledProcessError:
        ssids = []
    if not ssids:
        print("[!] No saved networks found via networksetup. Try running as root.")
        return results
    for ssid in ssids:
        try:
            pw_output = subprocess.check_output(["security", "find-generic-password", "-D", "AirPort network password", "-a", ssid, "-w"], text=True, stderr=subprocess.DEVNULL).strip()
            password = pw_output if pw_output else "(no password / open network)"
        except subprocess.CalledProcessError:
            password = "(not found in Keychain — may need permissions)"
        results.append({"ssid": ssid, "password": password})
    return results

def get_wifi_passwords_linux():
    results = []
    import os
    nm_dir = "/etc/NetworkManager/system-connections"
    if not os.path.isdir(nm_dir):
        print("[!] NetworkManager connections directory not found.")
        return results
    for fname in os.listdir(nm_dir):
        path = os.path.join(nm_dir, fname)
        try:
            with open(path, "r", errors="ignore") as f:
                content = f.read()
            ssid_match = re.search(r"ssid=(.+)", content)
            psk_match = re.search(r"psk=(.+)", content)
            ssid = ssid_match.group(1).strip() if ssid_match else fname
            password = psk_match.group(1).strip() if psk_match else "(no password / open or enterprise)"
            results.append({"ssid": ssid, "password": password})
        except Exception:
            continue
    return results

def print_results(results):
    if not results:
        print("[!] No Wi-Fi profiles found.")
        return
    max_ssid = max(len(r["ssid"]) for r in results)
    print(f"\n{'='*50}")
    print(f"  {'Network (SSID)':<{max_ssid}}   Password")
    print(f"  {'-'*max_ssid}   {'-'*30}")
    for r in results:
        print(f"  {r['ssid']:<{max_ssid}}   {r['password']}")
    print(f"{'='*50}\n")

def main():
    os_name = platform.system()
    print(f"\n[*] Wi-Fi Password Checker")
    print(f"[*] Detected OS: {os_name}")
    if os_name == "Windows":
        results = get_wifi_passwords_windows()
    elif os_name == "Darwin":
        results = get_wifi_passwords_macos()
    elif os_name == "Linux":
        results = get_wifi_passwords_linux()
    else:
        print(f"[!] Unsupported OS: {os_name}")
        sys.exit(1)
    print_results(results)

if __name__ == "__main__":
    main()
