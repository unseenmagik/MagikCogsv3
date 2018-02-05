import pathlib
import asyncio  # noqa: F401
import discord
from discord.ext import commands
from .dataIO import dataIO
from redbot.core import checks
from datetime import datetime

path = 'data/embedmaker'


class EmbedMaker:
    """
    Make embed objects. Recall them, remove them, reuse them (etc)
    """

    __original_auther__ = "mikeshardmind (Sinbad#0413)"
    __original_code__ = "https://github.com/mikeshardmind/SinbadCogs/tree/master/embedmaker"
    __original authers_license__ = "https://github.com/mikeshardmind/SinbadCogs/blob/master/License.md"
    __modified_by__ = "xDp64x"
    __version__ = "1.0.0"

    def __init__(self, bot):

        self.bot = bot
        self.settings = dataIO.load_json(path + '/settings.json')
        self.embeds = dataIO.load_json(path + '/embeds.json')

    def save_settings(self):
        dataIO.save_json(path + '/settings.json', self.settings)

    def save_embeds(self):
        dataIO.save_json(path + '/embeds.json', self.embeds)

    async def initial_config(self, server):
        """adds default settings for all servers the bot is in
        when needed and on join"""
        #server = ctx.guild
        #channel = ctx.channel

        if server:
            if server.id not in self.settings:
                self.settings[server.id] = {'inactive': False,
                                            'usercache': [],
                                            'roles': []
                                            }
                self.save_settings()

            if server.id not in self.embeds:
                self.embeds[server.id] = {'embeds': []}
                self.save_embeds()

        """if 'global' not in self.embeds:
            self.embeds['global'] = {'embeds': []}
            self.save_embeds()"""
        """if 'global' not in self.settings:
            self.settings['global'] = {'inactive': True,
                                       'usercache': [],
                                       'whitelist': []}  """# Future Proofing
        self.save_settings()

    @commands.group(name="embedset", pass_context=True, no_pm=True)
    async def embedset(self, ctx):
        server = ctx.guild
        print(server.id)
        """configuration settings"""

        em = discord.Embed(
            title='Commands for embedset',
            description='',
            color=0x207cee
        )
        em.add_field(
            name='toggleactive',
            value='Toggles whether embeds are enabled or not.',
            inline=False
        )
        """em.add_field(
            name='toggleglobal',
            value='Toggles whether global embeds are enabled or not. (Owner Only)',
            inline=False
        )"""
        msg = ctx.message.content[1:]
        if msg == 'embedset':
            await ctx.send(embed=em)

    @commands.group(name="embed", pass_context=True, no_pm=True)
    async def embed(self, ctx):
        """embed tools"""

        em = discord.Embed(
            title='Commands for embed',
            description='',
            color=0x207cee)
        em.add_field(
            name='list',
            value='Lists the embeds on this server',
            inline=False
        )
        em.add_field(
            name='remove',
            value='Removes an embed.',
            inline=False
        )
        """em.add_field(
            name='removeglobal',
            value='Removes a global embed. (Owner Only)',
            inline=False
        )"""
        em.add_field(
            name='make',
            value='Interactive prompt for making a embed',
            inline=False
        )
        """em.add_field(
            name='makeglobal',
            value='Interactive prompt for making a global embed.(Owner Only)',
            inline=False
        )"""
        em.add_field(
            name='fetch',
            value='Fetches an embed.',
            inline=False
        )
        """em.add_field(
            name='globalfetch',
            value='Fetches a global embed. (Owner Only)',
            inline=False
        )"""
        em.add_field(
            name='dm',
            value='Fetches an embed, DMs it to a user.',
            inline=False
        )
        em.add_field(
            name='reset',
            value='Clears user cache for the server only. Owner Only command.',
            inline=False
        )
        """em.add_field(
            name='globaldm',
            value='Fetches a global, DMs it to a user. (Owner Only)',
            inline=False
        )"""
        em.add_field(
            name='Example:',
            value='Run the command like this:\n``[p]embed make`` [p] being the prefix.',
            inline=False
        )
        msg = ctx.message.content[1:]
        if msg == 'embed':
            await ctx.send(embed=em)

    @embed.command(name="list", pass_context=True, no_pm=True)
    async def list_embeds(self, ctx):
        """lists the embeds on this server"""

        server = ctx.message.guild
        if server.id not in self.embeds:
            return await ctx.send("I couldn't find any embeds here")

        names = []
        for embed in self.embeds[server.id]["embeds"]:
            names.append(embed.get('name'))

        if len(names) > 0:
            await ctx.send("The following embeds "
                               "exist here:\n {}".format(names))
        else:
            await ctx.send("No embeds here.")

    @checks.admin_or_permissions(Manage_server=True)
    @embedset.command(name="toggleactive", pass_context=True, no_pm=True)
    async def embed_toggle(self, ctx):
        """Toggles whether embeds are enabled or not"""
        server = ctx.guild
        if server.id not in self.settings:
            await self.initial_config(server)
        self.settings[server.id]['inactive'] = \
            not self.settings[server.id]['inactive']
        self.save_settings()
        if self.settings[server.id]['inactive']:
            await ctx.send("Embeds disabled.")
        else:
            await ctx.send("Embeds enabled.")

    @checks.is_owner()
    @embedset.command(name="toggleglobal")
    async def global_embed_toggle(self, ctx):
        """Toggles whether global embeds are enabled or not"""
        if "global" not in self.settings:
            self.initial_config()
        self.settings['global']['inactive'] = \
            not self.settings['global']['inactive']
        self.save_settings()
        if self.settings['global']['inactive']:
            await ctx.send("Global Embeds disabled.")
        else:
            await ctx.send("Global Embeds enabled.")

    @checks.admin_or_permissions(Manage_messages=True)
    @embed.command(name="remove", pass_context=True, no_pm=True)
    async def remove_embed(self, ctx, name: str):
        """removes an embed"""
        server = ctx.guild
        name = name.lower()
        embeds = self.embeds[server.id]["embeds"]
        embeds[:] = [e for e in embeds if e.get('name') != name]
        self.embeds[server.id]["embeds"] = embeds
        self.save_embeds()
        await ctx.send("If an embed of that name existed, it is gone now.")

    @checks.is_owner()
    @embed.command(name="removeglobal", pass_context=True)
    async def remove_g_embed(self, ctx, name: str):
        """removes a global embed"""
        name = name.lower()
        embeds = self.embeds["global"]["embeds"]
        embeds[:] = [e for e in embeds if e.get('name') != name]
        self.embeds['global']["embeds"] = embeds
        self.save_embeds()
        await ctx.send("If an embed of that name existed, it is gone now.")

    @checks.admin_or_permissions(Manage_messages=True)
    @embed.command(name="make", pass_context=True, no_pm=True)
    async def make_embed(self, ctx, name: str):
        """Interactive prompt for making an embed"""
        author = ctx.message.author
        server = ctx.guild
        channel = ctx.channel

        if server.id not in self.embeds:
            await self.initial_config(server)
        if server.id not in self.settings:
            await self.initial_config(server)
        if self.settings[server.id]['inactive']:
            return await ctx.send("Embed creation is not currently "
                                      "enabled on this server.")

        name = name.lower()
        for e in self.embeds[server.id]['embeds']:
            if e.get('name') == name:
                return await ctx.send("An embed by that name exists ")

        if author.id in self.settings[server.id]['usercache']:
            return await ctx.send("Finish making your prior embed "
                                      "before making an additional one")

        await ctx.send("Preparing...")
        await self.contact_for_embed(ctx, name, author, channel, server)

    @checks.is_owner()
    @embed.command(name="makeglobal", pass_context=True)
    async def make_g_embed(self, ctx, name: str):
        """Interactive prompt for making a global embed"""
        author = ctx.message.author

        if "global" not in self.embeds:
            await self.initial_config()
        if "global" not in self.settings:
            await self.initial_config()

        name = name.lower()
        if name in self.embeds['global']['embeds']:
            return await ctx.send("An embed by that name exists ")

        if author.id in self.settings["global"]['usercache']:
            return await ctx.send("Finish making your prior embed "
                                      "before making an additional one")

        await ctx.send("I will message you to continue.")
        await self.contact_for_embed(name, author)

    @embed.command(name="fetch", pass_context=True, no_pm=True)
    async def fetch(self, ctx, name: str):
        """fetches an embed"""
        server = ctx.guild
        em = await self.get_embed(name.lower(), server.id)
        if em is None:
            return await ctx.send("I couldn't find an embed by that name.")
        await ctx.send(embed=em)

    @embed.command(name="fetchglobal", pass_context=True, no_pm=True)
    async def fetch_global(self, ctx, name: str):
        """fetches a global embed"""

        em = await self.get_embed(name.lower())
        if em is None:
            return await ctx.send("I couldn't find an embed by that name.")
        await ctx.send(embed=em)

    @checks.admin_or_permissions(Manage_messages=True)
    @embed.command(name="dm", pass_context=True, no_pm=True)
    async def fetch_dm(self, ctx, name: str, user_id: str):
        """fetches an embed, and DMs it to a user"""
        server = ctx.message.guild
        em = await self.get_embed(name.lower(), server.id)
        if em is None:
            return await ctx.send("I couldn't find an embed by that name.")
        who = await self.bot.get_user_info(user_id)
        if who is not None:
            await who.send(embed=em)

    @checks.is_owner()
    @embed.command(name="dmglobal", pass_context=True, no_pm=True)
    async def fetch_global_dm(self, ctx, name: str, user_id: str):
        """fetches a global embed, and DMs it to a user"""

        em = await self.get_embed(name.lower())
        if em is None:
            return await ctx.send("I couldn't find an embed by that name.")
        who = await self.bot.get_user_info(user_id)
        if who is not None:
            await self.bot.send_message(who, embed=em)
    @checks.is_owner()
    @embed.command(name='reset', pass_context=True, no_pm=True)
    async def _reset(self, ctx):
        """This is only to remove the temporary cache
        within the server the command is in."""
        server = ctx.guild
        try:
            self.settings[server.id]['usercache'] = []
            self.save_settings()
            await ctx.send("Reset complete.")
        except KeyError:
            await ctx.send("Error, nothing in the cache.")


    async def contact_for_embed(self, ctx, name: str, author, channel, server=None):
        if server is not None:
            self.settings[server.id]['usercache'].append(author.id)
        #else:
            #self.settings["global"]["usercache"].append(author.id)
        self.save_settings()

        await ctx.send("Please respond to this message with the title of your embed. If you do not want a title, wait 30s")
        await asyncio.sleep(1)
        def check(m):
            return m.author == author and m.channel == channel
        try:
            title = await self.bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.send("Okay, this one won't have a title.")
            title = " "

        dm = await ctx.send("Please respond to this message with the content of your embed. Timeout in 60s")
        await asyncio.sleep(1)
        try:
            message = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            print("Empty message")
            message = " "
        #if message is None:
            #if server is not None:
                #self.settings[server.id]['usercache'].remove(author.id)
            #else:
                #self.settings['global']['usercache'].remove(author.id)
            #self.save_settings()
            #return await ctx.send("I can't wait forever, try again when ready")
        #else:
        if title == " " and message == " " or message == " ":
            await ctx.send("Error in creating an embed. Both description and title are empty. Or description is empty.")
        else:
            await self.save_embed(name, title, message, server)
            await ctx.send("Your embed was created")

    async def get_embed(self, name: str, server_id=None):

        found = False
        if server_id is None:
            server_id = "global"
        if server_id in self.embeds:
            for embed in self.embeds[server_id]["embeds"]:
                if embed.get('name') == name:
                    title = embed.get('title')
                    content = embed.get('content')
                    #timestring = embed.get('timestamp', None)
                    #if timestring is None:
                        # old footer:
                        # message.timestamp.strftime('%Y-%m-%d %H:%M')
                        # footer = "created at {} UTC".format(timestamp)
                        # e.g. : "created at 2017-09-05 23:18 UTC"
                        #timestring = embed.get('footer')[11:-4]
                    #timestamp = datetime.strptime(timestring, '%Y-%m-%d %H:%M')
                    found = True

        if not found:
            return None

        em = discord.Embed(description=content, color=discord.Color.purple())
        if title is not None:
            em.set_author(name='{}'.format(title))
        return em

    async def save_embed(self, name, title, message, server=None):
        author = message.author
        content = message.clean_content
        if title != " ":
            title = title.clean_content
        #timestamp = message.timestamp.strftime('%Y-%m-%d %H:%M')
        name = name.lower()

        embed = {'name': name,
                 'title': title,
                 'content': content
                 #'timestamp': timestamp
                 }

        if server is not None:
            self.embeds[server.id]['embeds'].append(embed)
            self.settings[server.id]['usercache'].remove(author.id)
        #else:
            #self.embeds['global']['embeds'].append(embed)
            #self.settings['global']['usercache'].remove(author.id)
        self.save_embeds()

        self.save_settings()

