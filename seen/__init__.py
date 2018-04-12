from .dataIO import dataIO
import os
import asyncio
from .seen import Seen 

"""def __init__(self, bot):
    self.bot = bot
    self.seen = dataIO.load_json('data/seen/seen.json')
    self.new_data = False"""

def check_folder():
    if not os.path.exists('data/seen'):
        print('Creating data/seen folder...')
        os.makedirs('data/seen')

def check_file():
    f = 'data/seen/seen.json'
    dataIO.save_json(f, {})
    print('Creating default seen.json...')

def setup(bot):
    check_folder()
    check_file()
    n = Seen(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(n.data_writer())
    bot.add_cog(n)