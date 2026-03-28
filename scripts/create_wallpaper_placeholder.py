#!/usr/bin/env python3
"""Create placeholder wallpaper images for testing (static mode until you add real video)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WALLPAPER = ROOT / "wallpaper"

def main():
    try:
        from PIL import Image
        WALLPAPER.mkdir(parents=True, exist_ok=True)
        # 1920x1080 MHA-style dark placeholder
        img = Image.new("RGB", (1920, 1080), color=(25, 45, 70))
        img.save(WALLPAPER / "dark.png")
        img.save(WALLPAPER / "light.png")
        print("Created wallpaper/dark.png and wallpaper/light.png")
        print("Update manifest to use static wallpaper (image: wallpaper/dark.png) until you add .webm")
    except ImportError:
        print("Install Pillow: pip install Pillow")

if __name__ == "__main__":
    main()
