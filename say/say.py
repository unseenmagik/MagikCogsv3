import discord
from discord.ext import commands

class Say:
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def say(self, ctx): 
        """Make your bot say something in the channel you use the command in."""

        msg = ctx.message.content
        message = ctx.message
        author = ctx.message.author
        
        #This gets rid of the command "[p]say"
        msg = msg[5:]
        try:
            await message.delete()
            
        except discord.Forbidden:
            print("No permissions.")
            Msg = "Unable to delete the command message, I don't have the adminstrative permissions to do so."
            await ctx.send(author, Msg)
        await ctx.send(msg)
