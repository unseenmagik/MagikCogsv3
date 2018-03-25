from .Counter import Counter
#from .dataIO import dataIO
import os
from redbot.core.json_io import JsonIO
from pathlib import Path
import asyncio

dir = os.getcwd()
config_dir = Path(dir)
config_dir.mkdir(parents=True, exist_ok=True)
g = config_dir / 'data/counter/count.json'
f = config_dir / 'data/counter/count.txt'

def check_folder():
    if not os.path.exists('data/counter'):
        print('Creating data/counter folder...')
        os.makedirs('data/counter')


def check_file():
    if not g.exists():
        #print('Test1')
        #print('{}')
        return {
            "Author": "Ping",
            "Counter": 0
        }
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
    n = Counter(bot)
    #loop = asyncio.get_event_loop()
    #loop.create_task(n.data_writer())
    bot.add_listener(n.listener, 'on_message')
    bot.add_cog(n)