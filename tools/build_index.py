#!/usr/bin/env python3
"""Rebuilds index.json from every theme file in themes/ (free themes only), with the launcher's
newest version from launcher.json (copies not from Google Play check it from Settings)."""
import glob
import json
import os

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
themes = []
for path in sorted(glob.glob("themes/*.json")):
    with open(path) as f:
        theme = json.load(f)
    if "productId" in theme:
        raise SystemExit(f"{path}: free themes can't have a productId")
    themes.append(theme)
index = {"format": 1}
if os.path.exists("launcher.json"):
    with open("launcher.json") as f:
        index["launcher"] = json.load(f)
index.update({"themes": themes, "paid": []})
with open("index.json", "w") as f:
    json.dump(index, f, indent=2)
    f.write("\n")
print(f"index.json: {len(themes)} themes")
