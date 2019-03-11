from .tictactoe import Tictactoe


def setup(bot):
    n = Tictactoe()
    bot.add_cog(n)
