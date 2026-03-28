#!/usr/bin/env python3
"""Generate minimal placeholder audio files so the Opera GX mod loads.
Replace these with your MHA-themed sounds later."""

import wave
import struct
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLE_RATE = 44100
DURATION = 0.1  # 100ms of silence


def create_silent_wav(path: Path):
    """Create a minimal silent WAV file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        frames = int(SAMPLE_RATE * DURATION)
        wav.writeframes(b"\x00\x00" * frames)


def create_silent_mp3(path: Path):
    """Create minimal MP3 using pydub+ffmpeg if available, else WAV fallback."""
    try:
        from pydub import AudioSegment
        path.parent.mkdir(parents=True, exist_ok=True)
        silent = AudioSegment.silent(duration=int(DURATION * 1000))
        silent.export(str(path), format="mp3", bitrate="128k")
    except (ImportError, FileNotFoundError, Exception):
        # Fallback: create WAV (Opera GX supports WAV for sounds/music)
        wav_path = path.with_suffix(".wav")
        create_silent_wav(wav_path)
        print(f"  Created {wav_path} (install ffmpeg for MP3)")


def main():
    print("Generating placeholder audio for My Hero Academia mod...")

    # Keyboard sounds (WAV)
    keyboard_files = [
        "backspace.wav", "enter.wav",
        "letter_1.wav", "letter_2.wav", "letter_3.wav",
        "space.wav"
    ]
    for f in keyboard_files:
        p = ROOT / "keyboard" / f
        create_silent_wav(p)
        print(f"  Created {p.relative_to(ROOT)}")

    # Browser sounds (MP3 if ffmpeg available, else WAV)
    sound_files = [
        "click", "feature_switch_off", "feature_switch_on",
        "hover", "important_click", "level_upgrade",
        "limiter_off", "limiter_on", "switch",
        "close_tab", "new_tab", "tab_slash"
    ]
    for f in sound_files:
        p = ROOT / "sound" / f"{f}.mp3"
        create_silent_mp3(p)
        out = p if p.exists() and p.stat().st_size > 0 else ROOT / "sound" / f"{f}.wav"
        if out.exists():
            print(f"  Created {out.relative_to(ROOT)}")

    # Background music - 4 tracks for vertical remixing
    for i in range(1, 5):
        p = ROOT / "music" / f"track_{i}.mp3"
        create_silent_mp3(p)
        out = p if p.exists() and p.stat().st_size > 0 else ROOT / "music" / f"track_{i}.wav"
        if out.exists():
            print(f"  Created {out.relative_to(ROOT)}")

    print("\nDone! Replace these with your MHA-themed sounds.")
    print("For MP3 placeholders: pip install pydub (requires ffmpeg for full support)")


if __name__ == "__main__":
    main()
