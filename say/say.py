import discord
from discord.ext import commands
from redbot.core import checks

class Say:

    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(administrator=True)
    async def say(self, ctx): 
        """Make your bot say something in the channel you use the command in."""

        msg = ctx.message.content
        message = ctx.message
        author = ctx.message.author
        
        #This gets rid of the command "[p]say" or "[p]betasay" depending on the number...
        msg = msg[5:]
        #5: for just [p]say
        #8: for [p]betasay
        try:
            await message.delete()
            
        except discord.Forbidden:
            print("No permissions.")

            def error(self, ctx):
                embed=discord.Embed(
                    title="Error:",
                    description="Unable to delete the command message, I don't have the adminstrative permissions to do so.",
                    color=0x207cee)
                return embed           

            Msg = error(self, ctx)
            await author.send(embed=Msg)
        try:
            await ctx.send(msg)
        except discord.errors.HTTPException:
            def error2(self, ctx):
                embed=discord.Embed(
                    title="Error:",
                    description="Unable to send text. Its empty. :upside_down: ",
                    color=0x207cee)
                return embed
            Msg2 = error2(self, ctx)
            await author.send(embed=Msg2)
