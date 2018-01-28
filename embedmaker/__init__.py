from .embedmaker import EmbedMaker
from .dataIO import dataIO
import os
import pathlib

path = 'data/embedmaker'

def check_folder():
    if not os.path.exists('data/embedmaker'):
        print('Creating data/embedmaker folder...')
        os.makedirs('data/embedmaker')


def check_file():
    f = 'data/embedmaker/embeds.json'
    o = 'data/embedmaker/settings.json'
    dataIO.save_json(f, {})
    dataIO.save_json(o, {})
    print('Creating default embeds.json and settings.json...')


def setup(bot):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    check_file()
    n = EmbedMaker(bot)
    check_folder()
    bot.add_cog(n)
