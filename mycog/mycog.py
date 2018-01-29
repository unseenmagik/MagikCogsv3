from discord.ext import commands

class Mycog:
    """My custom cog"""

    @commands.command()
    async def mbv3(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Exciting new things coming with MagikBotv3f!")
