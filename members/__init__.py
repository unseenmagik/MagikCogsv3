from .members import Members

def setup(bot):
    bot.add_cog(Members(bot))