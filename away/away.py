import os
import discord
from .dataIO import dataIO
from redbot.core import checks
from discord.ext import commands

class Away:
    def __init__(self, bot):
        self.data = dataIO.load_json('data/away/away.json')
    """Le away cog"""

    async def listener(self, message):
        tmp = {}
        server = message.guild
        channel = message.channel
        if server.id not in self.data:
            for mention in message.mentions:
                tmp[mention] = True
            for author in tmp:
                if author.id in self.data:
                    try:
                        avatar = author.avatar_url if author.avatar else author.default_avatar_url
                        if self.data[author.id]['MESSAGE']:
                            em = discord.Embed(description=self.data[author.id]['MESSAGE'], color=discord.Color.blue())
                            em.set_author(name='{} is currently away'.format(author.display_name), icon_url=avatar)
                        else:
                            em = discord.Embed(color=discord.Color.blue())
                            em.set_author(name='{} is currently away'.format(author.display_name), icon_url=avatar)
                        await channel.send(embed=em)
                    except:
                        if self.data[author.id]['MESSAGE']:
                            msg = '{} is currently away and has set the following message: `{}`'.format(author.display_name, self.data[author.id]['MESSAGE'])
                        else:
                            msg = '{} is currently away'.format(author.display_name)
                        await channel.send(msg)

    @commands.command(pass_context=True, name="away")
    async def _away(self, context, *message: str):
        """Tell the bot you're away or back."""
        author = context.message.author
        if author.id in self.data:
            del self.data[author.id]
            msg = 'You\'re now back.'
        else:
            self.data[context.message.author.id] = {}
            self.data[context.message.author.id]['MESSAGE'] = ' '.join(context.message.clean_content.split()[1:])
            msg = 'You\'re now set as away.'
        dataIO.save_json('data/away/away.json', self.data)
        await context.send(msg)
