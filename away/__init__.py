from .away import Away
#from .dataIO import dataIO
import os
from redbot.core.json_io import JsonIO
from pathlib import Path

dir = os.getcwd()
config_dir = Path(dir)
config_dir.mkdir(parents=True, exist_ok=True)
g = config_dir / 'data/away/away.json'

def check_folder():
    if not os.path.exists('data/away'):
        print('Creating data/away folder...')
        os.makedirs('data/away')


def check_file():
    if not g.exists():
        #print('Test1')
        #print('{}')
        return {}
    return JsonIO(g)._load_json()
    print('Creating default away.json...')
def save_file():
    config = check_file()
    JsonIO(g)._save_json(config)

def load_file():
    JsonIO(g)._load_json()
    print('Loaded')
def setup(bot):
    check_folder()
    save_file()
    load_file()
    n = Away(bot)
    bot.add_listener(n.listener, 'on_message')
    bot.add_cog(n)