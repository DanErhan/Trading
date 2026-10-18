"""Build the FINAS site from site.template.html by inlining the map, logo and photo.

Writes two files:
  index.html     standalone page (open it in any browser)
  artifact.html  the same page without the document wrapper, for publishing as an artifact

Usage: python3 finas/build.py
"""
import base64
import pathlib
import re

HERE = pathlib.Path(__file__).parent
ASSETS = HERE / "assets"


def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def map_paths():
    svg = (ASSETS / "romania-map.svg").read_text()
    return re.sub(r"^<svg[^>]*>|</svg>$", "", svg.strip())


html = (HERE / "site.template.html").read_text()
html = (html.replace("%%MAP%%", map_paths())
            .replace("%%LOGO%%", data_uri(ASSETS / "fng-logo.jpg", "image/jpeg"))
            .replace("%%PHOTO%%", data_uri(ASSETS / "bess-site.jpg", "image/jpeg")))
(HERE / "artifact.html").write_text(html)
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '</head>\n<body>\n' + html + '\n</body>\n</html>\n')
(HERE / "index.html").write_text(page)
print(f"wrote index.html and artifact.html ({len(page) // 1024} KB)")
