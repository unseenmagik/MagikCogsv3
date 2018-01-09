import discord
from .utils import checks
from discord.ext import commands

class Say:
    """Make your bot say or upload something in the channel you want."""


    @commands.group(pass_context=True)
    async def send(self, ctx): # Had to choose something else than say :c have a better idea ?
        await ctx.send(ctx.message.channel, page)

    @send.command(pass_context=True)
    async def here(self, ctx, *, text):
        """Say a message in the actual channel"""
        
        message = ctx.message
        server = message.guild
