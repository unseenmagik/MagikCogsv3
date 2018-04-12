import os
import discord
from redbot.core.json_io import JsonIO
from discord.ext import commands
from pathlib import Path

class Away:
    def __init__(self, bot):
        dir = os.getcwd()
        config_dir = Path(dir)
        config_dir.mkdir(parents=True, exist_ok=True)
        g = config_dir / 'data/away/away.json'
        self.data = JsonIO(g)._load_json()
    """Le away cog"""

    async def listener(self, message):
        tmp = {}
        server = message.guild
        channel = message.channel
        #if server.id not in self.data:
        for mention in message.mentions:
            tmp[mention] = True
        for author in tmp:
            auth = str(author.id)
            if str(author.id) in self.data or author.id in self.data:
                avatar = author.avatar_url if author.avatar else author.default_avatar_url
                try:
                    em = discord.Embed(description=self.data[author.id]['MESSAGE'], color=discord.Color.blue())
                except:
                    em = discord.Embed(description=str(self.data[auth]['MESSAGE']), color=discord.Color.blue())
                em.set_author(name='{} is currently away'.format(author.display_name), icon_url=avatar)
                await channel.send(embed=em)

    @commands.command(pass_context=True, name="away")
    async def _away(self, context, *message: str):
        """Tell the bot you're away or back."""
        dir = os.getcwd()
        config_dir = Path(dir)
        config_dir.mkdir(parents=True, exist_ok=True)
        g = config_dir / 'data/away/away.json'
        author = context.message.author
        print(self.data)
        auth = str(author.id)
        ctxx = int(author.id)
        if author.id in self.data or str(author.id) in self.data:
            try:
                del self.data[author.id]
            except:
                del self.data[auth]
            msg = "You're now back."
        else:
            try:
                self.data[context.message.author.id] = {}
                self.data[context.message.author.id]['MESSAGE'] = ' '.join(context.message.clean_content.split()[1:])
            except:
                self.data[ctxx] = {}
                self.data[ctxx]['MESSAGE'] = ' '.join(context.message.clean_content.split()[1:])
            msg = "You're now set as away."
        JsonIO(g)._save_json(self.data)
        await context.send(msg)
