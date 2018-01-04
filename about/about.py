import discord
from discord.ext import commands

class About:
    """More information about Magik Bot"""
    

    @commands.command()
    async def about(self, ctx):
        """About Magik Bot"""
        
        embed=discord.Embed(title="About Magik Bot V3", url='http://www.magikbot.co.uk', description="The 3rd version of a discord bot made with love. Created for Discord Administration support. With hundreds of commands, admin, mod, support, games, fun and more. For more information see below:", color=0x545454)
        embed.set_author(name="Magik Bot V3", url='http://www.magikbot.co.uk', icon_url='https://cdn.discordapp.com/avatars/375541314139324416/054ca0e904c2120658a1d31623819703.png?size=1024')
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/375541314139324416/054ca0e904c2120658a1d31623819703.png?size=1024')
        embed.add_field(name="Discord Support", value="https://discord.gg/kQjTw5Z", inline=True)
        embed.add_field(name="Website", value="http://www.magikbot.co.uk", inline=True)
        embed.add_field(name="Auther", value="Magik#0203", inline=False)
        embed.add_field(name="Discord & API Version", value="Discord - 3.5.2 & API version 1.0.0a", inline=True)
        embed.set_footer(text="Magik Bot - Providing Discord support since September 2017")
        
        await ctx.send(embed=embed)
       
