# Wallpaper Files

| File | Description |
|------|-------------|
| `infinite100.mp4` | Animated wallpaper (dark + light themes use this path in `manifest.json`) |
| `dark.png` | First-frame thumbnail for dark theme |
| `light.png` | First-frame thumbnail for light theme |

Regenerate PNGs after changing the video:

```bash
python scripts/extract_first_frame.py
```

Optional: `--frame N` for a later frame if the first is black. You can also use separate `dark.webm` / `light.webm` or `dark.mp4` / `light.mp4` — see `scripts/extract_first_frame.py` search order.
