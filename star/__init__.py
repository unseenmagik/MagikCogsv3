from .star import Star
from redbot.cogs.star.dataIO import dataIO
from redbot.cogs.star.dataIO import fileIO
import os
import re

def __init__(self, bot):
    self.bot = bot
    self.settings = dataIO.load_json("data/star/settings.json")
        
            
def check_folder():
    if not os.path.exists('data/star'):
        print('Creating data/star folder...')
        os.makedirs('data/star')
            
def check_file():
    f = 'data/star/settings.json'
    dataIO.save_json(f, {})
    fileIO(f, 'save', {})
        
def setup(bot):
    check_folder()
    check_file()
    n = Star(bot)
    bot.add_listener(n.listener, 'on_message')
    bot.add_cog(n)
