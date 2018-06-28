import discord
import aiohttp
import io
from discord.ext import commands
from redbot.core import checks 
    
    @commands.command()
    @checks.is_owner()
    async def botinfo(self, ctx):
        """Prints nice bot info command"""

    async def on_guild_join(self, guild):
        channel = self.bot.get_channel(366758942212358145)
        online = len([m.status for m in guild.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle])
        total_users = len(guild.members)
        text_channels = len([x for x in guild.text_channels])
        voice_channels = len([x for x in guild.voice_channels])
        passed = (datetime.datetime.utcnow() - guild.created_at).days
        created_at = ("TrustyBot is on {} servers now! \nServer created {}. That's over {} days ago!"
                      "".format(len(self.bot.guilds), guild.created_at.strftime("%d %b %Y %H:%M"),
                                passed))

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        em = discord.Embed(
            description=created_at,
            colour=discord.Colour(value=colour),
            timestamp=guild.created_at)
        em.add_field(name="Region", value=str(guild.region))
        em.add_field(name="Users", value="{}/{}".format(online, total_users))
        em.add_field(name="Text Channels", value=text_channels)
        em.add_field(name="Voice Channels", value=voice_channels)
        em.add_field(name="Roles", value=len(guild.roles))
        em.add_field(name="Owner", value="{} | {}".format(str(guild.owner), guild.owner.mention))
        if guild.features != []:
            em.add_field(name="Guild Features", value=", ".join(feature for feature in guild.features))
        em.set_footer(text="guild ID: {}".format(guild.id))

        if guild.icon_url:
            em.set_author(name=guild.name, icon_url=guild.icon_url)
            em.set_thumbnail(url=guild.icon_url)
        else:
            em.set_author(name=guild.name) 
        await channel.send(embed=em)
