#!/usr/bin/env python3
"""Extract a frame from wallpaper videos as PNG (OpenCV; no ffmpeg required)."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WALL = ROOT / "wallpaper"

DARK_CANDIDATES = ("dark.webm", "dark.mp4", "infinite100.mp4")
LIGHT_CANDIDATES = ("light.webm", "light.mp4")


def find_wallpaper_video(prefer_light: bool) -> Path | None:
    order = LIGHT_CANDIDATES if prefer_light else DARK_CANDIDATES
    for name in order:
        p = WALL / name
        if p.exists():
            return p
    if prefer_light:
        for name in DARK_CANDIDATES:
            p = WALL / name
            if p.exists():
                return p
    return None


def extract_frame(video: Path, out: Path, frame_one_based: int, cv2) -> bool:
    """frame_one_based: 1 = first frame, 30 = 30th frame."""
    idx = frame_one_based - 1
    if idx < 0:
        raise ValueError("frame must be >= 1")

    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        print(f"Could not open: {video}")
        return False

    cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
    ret, frame = cap.read()
    if not ret or frame is None:
        cap.release()
        print(f"Could not read frame {frame_one_based} from {video.name}")
        return False

    cap.release()
    out.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out), frame)
    return True


def main():
    p = argparse.ArgumentParser(description="Extract a frame from wallpaper video to PNG.")
    p.add_argument(
        "--frame",
        type=int,
        default=1,
        metavar="N",
        help="1-based frame number (default: 1 = first frame)",
    )
    args = p.parse_args()

    try:
        import cv2
    except ImportError:
        print("Installing opencv-python...")
        import subprocess

        subprocess.check_call(["pip", "install", "opencv-python", "-q"])
        import cv2

    dark_v = find_wallpaper_video(prefer_light=False)
    if dark_v is None:
        print(f"No wallpaper video found in {WALL} (tried {', '.join(DARK_CANDIDATES)})")
        return 1

    ok = extract_frame(dark_v, WALL / "dark.png", args.frame, cv2)
    if ok:
        print(f"Wrote {WALL / 'dark.png'} from {dark_v.name} (frame {args.frame})")

    light_v = find_wallpaper_video(prefer_light=True)
    if light_v is not None and light_v.resolve() != dark_v.resolve():
        ok2 = extract_frame(light_v, WALL / "light.png", args.frame, cv2)
        if ok2:
            print(f"Wrote {WALL / 'light.png'} from {light_v.name} (frame {args.frame})")
    elif ok:
        shutil.copy2(WALL / "dark.png", WALL / "light.png")
        print(f"Copied to {WALL / 'light.png'} (same source as dark)")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
