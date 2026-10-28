#!/usr/bin/env python3
"""
Audio Loudness Analyzer
Analyzes a WAV file and reports average loudness (dBFS) and peak levels.
"""

import sys
import wave
import numpy as np

def analyze_audio(filepath):
    with wave.open(filepath, 'rb') as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        raw = wf.readframes(n_frames)

    if sampwidth == 2:
        dtype = np.int16
        max_val = 32768.0
    elif sampwidth == 4:
        dtype = np.int32
        max_val = 2147483648.0
    else:
        print(f"Unsupported sample width: {sampwidth}")
        return

    data = np.frombuffer(raw, dtype=dtype).astype(np.float64)
    if n_channels > 1:
        data = data.reshape(-1, n_channels).mean(axis=1)

    # RMS loudness
    rms = np.sqrt(np.mean(data ** 2))
    if rms > 0:
        dbfs = 20 * np.log10(rms / max_val)
    else:
        dbfs = -np.inf

    peak = np.max(np.abs(data))
    peak_db = 20 * np.log10(peak / max_val) if peak > 0 else -np.inf

    print(f"File          : {filepath}")
    print(f"Sample rate   : {framerate} Hz")
    print(f"Channels      : {n_channels}")
    print(f"Duration      : {n_frames / framerate:.2f} s")
    print(f"Average (RMS) : {dbfs:.2f} dBFS")
    print(f"Peak          : {peak_db:.2f} dBFS")

    print("\nPeak thresholds exceeded:")
    for thresh in range(10, 140, 10):
        if peak_db > -thresh:
            print(f"  > -{thresh} dB")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audio_loudness_analyzer.py <file.wav>")
        sys.exit(1)
    analyze_audio(sys.argv[1])
