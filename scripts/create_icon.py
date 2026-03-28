#!/usr/bin/env python3
"""Create a minimal 512x512 placeholder icon for the mod."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICON_PATH = ROOT / "icon_placeholder.png"

def main():
    try:
        from PIL import Image
        img = Image.new("RGB", (512, 512), color=(34, 139, 34))  # MHA green
        img.save(ICON_PATH)
        print(f"Created {ICON_PATH}")
    except ImportError:
        print("Install Pillow for icon: pip install Pillow")
        print("Or add your own 512x512 PNG and set manifest.json → icons.512")

if __name__ == "__main__":
    main()
