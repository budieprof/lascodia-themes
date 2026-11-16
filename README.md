# Lascodia Launcher themes

The theme gallery for Lascodia Launcher: every theme in
**Themes → Browse gallery** comes from [`index.json`](index.json) in this repository.

A theme is a small JSON file: colours, shapes, a font and built-in features to switch on (such as an
aurora background or chime sounds). Themes are data only and can't run code. The launcher checks
every theme before showing it, and skips any it doesn't understand.

## Adding a theme

1. Add the theme file to [`themes/`](themes) (the format is described below).
2. Rebuild the index: `python3 tools/build_index.py`
3. Commit both. The launcher reads the new index the next time someone opens the gallery.

## Theme file format

```json
{
  "id": "aurora-live",
  "name": "Aurora Live",
  "author": "Your name",
  "format": 1,
  "colors": {
    "ground": "#04121F", "panel": "#062A3A", "text": "#FFFFFF", "muted": "#D2F5EE",
    "accent": "#3FE0C0", "onAccent": "#03201A", "focus": "#FFFFFF"
  },
  "surface": "liquid-glass",
  "font": "sans",
  "corner": 34,
  "artStrength": 1.0,
  "features": ["ambient-motion", "big-clock"]
}
```

- `id`: lower-case letters, digits and `-`, unique.
- `surface`: `liquid-glass`, `frost`, `solid`, `none`, `paper`, `pixel` or `flat`.
- `font`: `sans`, `condensed`, `mono` or `serif`.
- `corner`: 0–48. `artStrength`: 0.0–1.0.
- `features`: `ambient-motion`, `aurora`, `big-clock`, `shelf-library`, `scanlines`, `monochrome`,
  `chime`, `tilt`.

`index.json` also has a `paid` list for premium themes; it's empty while purchases aren't available.
