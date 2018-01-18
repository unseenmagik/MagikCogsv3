from discord.ext import commands
import discord
import gpxpy.geo
import math
#from math import sin, cos, sqrt, atan2, radians

class Distance:
    """Calculate the distance between two coordinates."""

    @commands.command(pass_context = True)
    async def distance(self, ctx, *, message):
        """Calculate the distance between two coordinates."""
        # Your code will go here

        def error_embed_1(self):
            embed=discord.Embed(
                title="Error:",
                description="Not enough data given. Did you give 4 different coordinates, seperated by spaces?",
                color=0x207cee)
            return embed
        def error_embed_2(self):
            embed=discord.Embed(
                title="Error:",
                description="Your message is invalid. Please use this format\n``!distance <num1> <num2> <num3> <num4>``\nWhich would look like this: ``!distance 51.301597 -0.598019 51.270664 -0.594132``",
                color=0x207cee)
            return embed

        def calc_embed(msg, msg2):
            embed=discord.Embed(
                title="Distance Calculation",
                description=" ",
                color=0x207cee)
            embed.add_field(
                name="**Calculated Distance:**",
                value="{} kilometers".format(msg),
                inline=False)
            embed.add_field(
                name="**Cooldown Timer:**", 
                value="{} ".format(msg2),
                inline=False)
            return embed

        def calculate(lon1, lat1, lon2, lat2):
            dist = gpxpy.geo.haversine_distance(lat1, lon1, lat2, lon2)
            dist = dist/1000
            dist = round(dist, 2)
            
            return dist

        def cooldown(dist):
            time = " "

            
            if dist >= 1500:
                time = "120 min"

            elif dist >= 1000 and dist <= 1500:
                time = "90 min"

            elif dist >= 820 and dist <= 1000:
                time = "85 min"

            elif dist >= 720 and dist <= 820:
                time = "80 min"

            elif dist >= 700 and dist <= 720:
                time = "75 min"

            elif dist >= 565 and dist <= 700:
                time = "67 min"

            elif dist >= 500 and dist <= 565:
                time = "60 min"

            elif dist >= 460 and dist <= 500:
                time = "58 min"

            elif dist >= 345 and dist <= 460:
                time = "50 min"

            elif dist >= 250 and dist <= 345:
                time = "45 min"

            elif dist >= 220 and dist <= 250:
                time = "40 min"

            elif dist >= 100 and dist <= 220:
                time = "35 min"

            elif dist >= 80 and dist <= 100:
                time = "27 min"

            elif dist >= 75 and dist <= 80:
                time = "25 min"

            elif dist >= 65 and dist <= 75:
                time = "22 min"

            elif dist >= 40 and dist <= 65:
                time = "19 min"

            elif dist >= 35 and dist <= 40:
                time = "17 min"

            elif dist >= 30 and dist <= 35:
                time = "15 min"

            elif dist >= 20 and dist <= 30:
                time = "10 min"

            elif dist >= 15 and dist <= 20:
                time = "8 min"

            elif dist >= 10 and dist <= 15:
                time = "7 min"

            elif dist >= 8 and dist <= 10:
                time = "6 min"

            elif dist >= 5 and dist <= 8:
                time = "2 min 30 sec min"

            elif dist >= 4 and dist <= 5:
                time = "2 min"

            elif dist >= 3 and dist <= 4:
                time = "2 min"

            elif dist >= 2 and dist <= 3:
                time = "1 min 30 sec"

            elif dist >= 1 and dist <= 2:
                time = "1 min 30 sec"

            elif dist and dist <= 1:
                time = "1 min"
                      
            return time

        bool = True
        List = str(message)
        var = List.split(" ")
        try:
            lat1 = float(var[0])
            long1 = float(var[1])

            lat2 = float(var[2])
            long2 = float(var[3])

        except IndexError:
            msg = error_embed_1(self)
            bool = False
        
        except ValueError:
            msg = error_embed_2(self)
            bool = False

        if bool == True:
            calc = calculate(long1, lat1, long2, lat2)
            cooldown = cooldown(calc)
            msg = calc_embed(calc, cooldown)
        await ctx.send(embed=msg)



