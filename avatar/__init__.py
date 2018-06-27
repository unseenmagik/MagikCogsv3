from .avatar import Avatar
from redbot.core import data_manager

def setup(bot):
    n = Avatar(bot)
    data_manager.load_bundled_data(n, __file__)
    bot.add_cog(n)
