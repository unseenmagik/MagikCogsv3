import os

from discord.ext import commands
from random import randint

from .utils.dataIO import dataIO
from .utils import checks


def __init__(self, bot):
    self.bot = bot
    self.path = "data/Fox-Cogs/hangman"
    self.file_path = "data/Fox-Cogs/hangman/hangman.json"
    self.answer_path = "data/hangman/hanganswers.txt"
    self.the_data = dataIO.load_json(self.file_path)
    self.winbool = False
    self.letters = "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"
    self.navigate = "🔼🔽"
    self._updateHanglist()

def check_folders():
    if not os.path.exists("data/Fox-Cogs"):
        print("Creating data/Fox-Cogs folder...")
        os.makedirs("data/Fox-Cogs")

    if not os.path.exists("data/Fox-Cogs/hangman"):
        print("Creating data/Fox-Cogs/hangman folder...")
        os.makedirs("data/Fox-Cogs/hangman")

        
def check_files():
    if not dataIO.is_valid_json("data/Fox-Cogs/hangman/hangman.json"):
        dataIO.save_json("data/Fox-Cogs/hangman/hangman.json", {"running": False, "hangman": 0, "guesses": [], "theface": "<:never:336861463446814720>", "trackmessage": False})



def setup(bot):
    check_folders()
    check_files()
    n = Hangman(bot)
    bot.add_listener(n._on_react, "on_reaction_add")
    bot.add_cog(n)
