from .botinfo import Botinfo

def setup(bot):
    bot.add_cog(Botinfo(bot))
