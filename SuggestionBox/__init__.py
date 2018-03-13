from .suggestionbox import SuggestionBox
from .dataIO import dataIO
import os
from pathlib import Path
from redbot.core.json_io import JsonIO

dir = os.getcwd()
config_dir = Path(dir)
config_dir.mkdir(parents=True, exist_ok=True)
g = config_dir / 'data/suggestionbox/settings.json'

def check_folder():
    f = 'data/suggestionbox'
    if not os.path.exists(f):
        os.makedirs(f)

def check_file():
    if not g.exists():
        return {}
    return JsonIO(g)._load_json()

def save_file():
    config = check_file()
    JsonIO(g)._save_json(config)

def load_file():
    JsonIO(g)._load_json()
    print('Loaded...')


def setup(bot):
    check_folder()
    save_file()
    load_file()
    n = SuggestionBox(bot)
    bot.add_cog(n)