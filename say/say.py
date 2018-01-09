import discord
from discord.ext import commands

class Say:
    """Make your bot say something in the channel you want."""


    @commands.command(pass_context=True)
    async def send(self, ctx): 
        """This does stuff!"""
        msg = ctx.message.content
        message = ctx.message
        server = message.guild
        channel = ctx.channel
        
        #This gets rid of the command "[p]send"
        msg = msg[6:]

        await message.delete()
        await ctx.send(msg)
