import discord
from .utils import checks
from discord.ext import commands

class Say:
    """Make your bot say or upload something in the channel you want."""


    @commands.command()
    async def send(self, ctx): 
        """This does stuff!"""
        # Your code will go here
        await ctx.send("The bot will say what i want it to say")

