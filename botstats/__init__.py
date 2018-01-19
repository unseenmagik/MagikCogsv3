from .botstats import BotStats
from .dataIO import dataIO
import os

"""def __init__(self, bot):
    self.bot = bot
    self.derp = "data/botstats/json.json"
    self.imagenius = dataIO.load_json(self.derp)"""
        
def check_folders():
    if not os.path.exists("data/botstats"):
        print("Creating the botstats folder, so be patient...")
        os.makedirs("data/botstats")
        print("Finish!")

def check_files():
    twentysix = "data/botstats/json.json"
    json = {
        "MAINPREFIX" : "This can be set when starting botstats thru [p]botstats toggle",
        "TOGGLE" : False,
        "SECONDS2LIVE" : 15,
        "MESSAGE" : "{0}help | {1} servers | {2} users"
    }

    if not dataIO.is_valid_json(twentysix):
        print("Derp Derp Derp...")
        dataIO.save_json(twentysix, json)
        print("Created json.json!")

def setup(bot):

    check_folders()
    check_files()
    bot.add_cog(BotStats(bot))
