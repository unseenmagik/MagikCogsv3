from redbot.core import commands
#from discord.ext import commands
import discord
import gpxpy.geo
import math
#from math import sin, cos, sqrt, atan2, radians

class Distance(commands.Cogs:
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
                title="",
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
                time = "120 minutes"

            elif dist >= 1403 and dist <= 1500:
                time = "120 minutes"

            elif dist >= 1344 and dist <= 1403:
                time = "119 minutes"

            elif dist >= 1300 and dist <= 1344:
                time = "117 minutes"

            elif dist >= 1221 and dist <= 1300:
                time = "112 minutes"

            elif dist >= 1180 and dist <= 1221:
                time = "109 minutes"

            elif dist >= 1020 and dist <= 1180:
                time = "101 minutes"

            elif dist >= 1007 and dist <= 1020:
                time = "97 minutes"

            elif dist >= 948 and dist <= 1007:
                time = "94 minutes"

            elif dist >= 897 and dist <= 948:
                time = "90 minutes"

            elif dist >= 839 and dist <= 897:
                time = "88 minutes"

            elif dist >= 802 and dist <= 839:
                time = "83 minutes"

            elif dist >= 751 and dist <= 802:
                time = "81 minutes"

            elif dist >= 700 and dist <= 751:
                time = "76 minutes"

            elif dist >= 650 and dist <= 700:
                time = "73 minutes"

            elif dist >= 600 and dist <= 650:
                time = "69 minutes"

            elif dist >= 550 and dist <= 600:
                time = "65 minutes"

            elif dist >= 500 and dist <= 550:
                time = "61 minutes"

            elif dist >= 450 and dist <= 500:
                time = "58 minutes"

            elif dist >= 400 and dist <= 450:
                time = "54 minutes"

            elif dist >= 350 and dist <= 400:
                time = "49 minutes"

            elif dist >= 328 and dist <= 350:
                time = "48 minutes"

            elif dist >= 300 and dist <= 328:
                time = "46 minutes"

            elif dist >= 250 and dist <= 300:
                time = "41 minutes"

            elif dist >= 201 and dist <= 250:
                time = "36 minutes"

            elif dist >= 175 and dist <= 201:
                time = "33 minutes"

            elif dist >= 150 and dist <= 175:
                time = "31 minutes"
                
            elif dist >= 125 and dist <= 150:
                time = "28 minutes"
                
            elif dist >= 100 and dist <= 125:
                time = "26 minutes"

            elif dist >= 90 and dist <= 100:
                time = "24 minutes"
                
            elif dist >= 80 and dist <= 90:
                time = "23 minutes"
                
            elif dist >= 70 and dist <= 80:
                time = "22 minutes"
                
            elif dist >= 60 and dist <= 70:
                time = "21 minutes"
                
            elif dist >= 50 and dist <= 60:
                time = "20 minutes"
                
            elif dist >= 45 and dist <= 50:
                time = "19 minutes" 
                
            elif dist >= 40 and dist <= 45:
                time = "18 minutes"
                
            elif dist >= 35 and dist <= 40:
                time = "17 minutes"
                
            elif dist >= 30 and dist <= 35:
                time = "16 minutes"
                
            elif dist >= 25 and dist <= 30:
                time = "14 minutes"
                
            elif dist >= 20 and dist <= 25:
                time = "11 minutes"
                
            elif dist >= 15 and dist <= 20:
                time = "8 minutes"
                
            elif dist >= 10 and dist <= 15:
                time = "6 minutes" 
                
            elif dist >= 8 and dist <= 10:
                time = "4 minutes"
                
            elif dist >= 5 and dist <= 8:
                time = "3 minutes"
                
            elif dist >= 4 and dist <= 5:
                time = "2 minutes"   
                
            elif dist >= 3 and dist <= 4:
                time = "2 minutes"
                
            elif dist >= 2 and dist <= 3:
                time = "1 minutes"                

            elif dist >= 1 and dist <= 2:
                time = "48 seconds"
                      
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



