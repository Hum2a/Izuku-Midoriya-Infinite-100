# Izuku Midoriya - Infinite 100 — Opera GX mod

Season 4 / Overhaul arc energy: green-and-black GX theme, subtle Eri gold glow in web styling, shaders **Eri Blessing** and **Infinite 100**, plus site-specific CSS. Background music: `music/Deku-vs-Overhaul.mp3`. Icon: `infinite100_icon.png` (512×512). Swap wallpaper if you like.

## Structure

```
OperaGX/
├── manifest.json          # Mod configuration
├── infinite100_icon.png   # Icon (512×512) for GX / manifest
├── license.txt
├── wallpaper/             # Animated wallpapers
│   ├── dark.webm, dark.png
│   └── light.webm, light.png
├── music/                 # Background music (MP3/WAV; list in `manifest.json`)
├── sound/                 # Browser sounds (clicks, tabs, etc.)
├── keyboard/              # Keyboard typing sounds
├── shader/                # Shaders: Eri Blessing, Infinite 100
├── webmodding/            # `deku-infinite100.css` (global), `sites-01`…`06`, `deku-infinite-opera.css`
└── scripts/               # Helper scripts
```

## Checklist: What You Need to Add

1. **Wallpaper** (placeholder included)
   - Currently uses static `wallpaper/dark.png` and `wallpaper/light.png`
   - For **animated**: add `dark.webm` + `dark.png` (first frame), then update manifest:
     ```json
     "image": "wallpaper/dark.webm",
     "first_frame": "wallpaper/dark.png"
     ```

2. **Icon** (placeholder included)
   - Run `python scripts/create_icon.py` to generate, or add your own 512×512px

3. **Sounds** (optional)
   - Placeholder silent audio is included. Replace with MHA-themed sounds:
   - **Browser sounds**: `sound/*.wav` (click, hover, tab_close, etc.)
   - **Keyboard sounds**: `keyboard/*.wav` (letter, space, enter, backspace)
   - **Background music**: paths in `manifest.json` → `background_music` (e.g. `music/Deku-vs-Overhaul.mp3`)

4. **Music format**: WAV or MP3 both work. For MP3, install ffmpeg and run `python scripts/generate_placeholders.py` to regenerate.

## Creating Your Wallpaper

**WebM from video:**
```bash
ffmpeg -i your_video.mp4 -c:v libvpx-vp9 -b:v 2M -an wallpaper/dark.webm
ffmpeg -i wallpaper/dark.webm -vframes 1 wallpaper/dark.png
```

## Load & Test

1. Open `opera:extensions` in Opera GX
2. Enable **Developer mode** (top right)
3. Click **Load unpacked** → select this folder
4. Open `opera:mods` to enable your mod

## Publish

- **Local share**: Pack extension in `opera:extensions` → produces .CRX file
- **GX.store**: [GX.create](https://create.gx.games/mods)

## Theme Customization

GX accent is a slightly punchier green (HSL ~148, 88%, 52% dark). Web pages also layer **gold mist** and **cool gray** in `deku-infinite100.css` for the Eri nod. Edit `manifest.json` → `mod.payload.theme` or the CSS variables to taste.

## Shaders

- **Eri Blessing**: Warm green-gold screen tint (SkSL)
- **Infinite 100**: Animated wave / surge

Toggle in mod settings.
