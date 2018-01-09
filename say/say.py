import discord
from discord.ext import commands

class Say:
    """Make your bot say something in the channel you want."""


    @commands.command()
    async def send(self, ctx): 
        """This does stuff!"""
        # Your code will go here
        if ctx.invoked_subcommand is None
        pages = self.bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            await ctx.send(ctx.message.channel, page)



