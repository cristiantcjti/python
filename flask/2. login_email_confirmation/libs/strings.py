"""
libs.strings
By default, uses `en-gb.json` file inside the `strings` top-level folder.
If language changes, set `libs.strings.default_locale` and run `libs.strings.refresh()`.
"""
import json

default_locale = "en-gb"
cached_strings = {}


def refresh():
    print("Refreshing...")
    global cached_strings
    with open(f"/home/cristian/Desktop/Flask/Classes/section_4/strings/{default_locale}.json") as f:
        cached_strings = json.load(f)


def gettext(name):
    return cached_strings[name]


def set_default_locale(locale):
    global default_locale
    default_locale = locale


refresh()
