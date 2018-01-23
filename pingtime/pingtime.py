import discord
from discord.ext import commands
import datetime
import time
from random import choice, randint
class Pingtime:
    """Ping the bot and display response time."""


    @commands.command(pass_context=True)
    async def pingtime(self, ctx):

        """Ping the bot and display response time."""
        print("Ping Test")
        await ctx.send ('__*`Pinging...`*__')
        t1 = time.perf_counter()
        print("T1: ", t1)

        
        
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        t2 = time.perf_counter()
        print("T2: ", t2)
        t3 = str((t2-t1) * 1000)
        print("T3: ", t3)
        t3 = t3[2:4]
        #thedata = ("**Pong.**\nMessage Latency: " + t3 + "ms")
        data = discord.Embed(description='**Pong.**\nMessage Latency: {}ms'.format(t3), colour=discord.Colour(value=color))
        

    
        await ctx.send(embed=data)
