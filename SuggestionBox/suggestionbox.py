import os
import asyncio  # noqa: F401
import discord
from discord.ext import commands
from .dataIO import dataIO
import time
from redbot.core import checks
from pathlib import Path
from redbot.core.json_io import JsonIO

dir = os.getcwd()
config_dir = Path(dir)
config_dir.mkdir(parents=True, exist_ok=True)
g = config_dir / 'data/suggestionbox/settings.json'

class SuggestionBox:
    """custom cog for a configureable suggestion box"""

    __author__ = "mikeshardmind"
    __version__ = "1.4.2"

    def __init__(self, bot):
        self.bot = bot
        self.settings = JsonIO(g)._load_json()
        #self.settings = dataIO.load_json('data/suggestionbox/settings.json')
        for s in self.settings:
            self.settings[s]['usercache'] = []

    def save_json(self):
        JsonIO(g)._save_json(self.settings)
        #dataIO.save_json("data/suggestionbox/settings.json", self.settings)

    @commands.group(name="setsuggest", pass_context=True, no_pm=True)
    async def setsuggest(self, ctx):
        prefix = ctx.prefix
        """configuration settings"""
        """if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)"""
        msg = ctx.message.content
        msg = msg[10:]
        em = discord.Embed(
            title="Subcommands",
            description="Here are the sub commands for 'suggest'",
            color=discord.Color.blue()
        )
        em.add_field(
            name="**output**",
            value="Set the output to channel(s).\nExample: ``{}setsuggest output #<channel>``".format(prefix),
            inline=False
        )
        em.add_field(
            name="**toggleactive**",
            value="Toggles whether the suggestion box is active.\nExample: ``{}setsuggest toggleactive``".format(prefix)
        )
        if msg == "t":
            await ctx.send(embed=em)


    def initial_config(self, server_id):
        """makes an entry for the server, defaults to turned on"""

        if server_id not in self.settings:
            self.settings[server_id] = {'inactive': False,
                                        'output': [],
                                        'cleanup': False,
                                        'usercache': [],
                                        'multiout': False
                                        }
            self.save_json()

    @checks.admin_or_permissions(Manage_server=True)
    @setsuggest.command(name="output", pass_context=True, no_pm=True)
    async def setoutput(self, ctx, chan: discord.TextChannel):
        """sets the output channel(s)"""
        server = ctx.message.guild
        if server.id not in self.settings:
            self.initial_config(server.id)
        if server != chan.guild:
            return await ctx.send("Stop trying to break this")
            #return await self.bot.say("Stop trying to break this")
        #if chan.type != discord.ChannelType.text:
            #return await ctx.send("That isn't a text channel")
            #return await self.bot.say("That isn't a text channel")
        if chan.id in self.settings[server.id]['output']:
            return await ctx.send("Channel already set as output")

        if self.settings[server.id]['multiout']:
            self.settings[server.id]['output'].append(chan.id)
            self.save_json()
            return await ctx.send("Channel added to output list")

        else:
            self.settings[server.id]['output'] = [chan.id]
            self.save_json()
            return await ctx.send("Channel set as output")

    @checks.admin_or_permissions(Manage_server=True)
    @setsuggest.command(name="toggleactive", pass_context=True, no_pm=True)
    async def suggest_toggle(self, ctx):
        """Toggles whether the suggestion box is enabled or not"""
        server = ctx.message.guild
        if server.id not in self.settings:
            self.initial_config(server.id)
        self.settings[server.id]['inactive'] = \
            not self.settings[server.id]['inactive']
        self.save_json()
        if self.settings[server.id]['inactive']:
            await ctx.send("Suggestions disabled.")

        else:
            await ctx.send("Suggestions enabled.")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(name="suggest", pass_context=True)
    async def makesuggestion(self, ctx):
        bool = True
        "make a suggestion by following the prompts"
        author = ctx.message.author
        server = ctx.message.guild
        channel = ctx.message.channel

        if server.id not in self.settings:
            return await ctx.send("Suggestion submissions have not been configured for this server.")

        if self.settings[server.id]['inactive']:
            return await ctx.send("Suggestion submission is not currently enabled on this server.")

        if author.id in self.settings[server.id]['usercache']:
            return await ctx.send("Finish making your prior suggestion before making an additional one.")

        #await self.bot.say("I will message you to collect your suggestion.")
        await ctx.send("I will message you to collect your suggestion.")
        self.settings[server.id]['usercache'].append(author.id)
        self.save_json()
        dm = await author.send(
                                         "Please respond to this message"
                                         " with your suggestion.\nYour "
                                         "suggestion should be a single "
                                         "message")

        def check2(m):
            return m.author == author and m.channel == dm.channel

        try:
            message = await self.bot.wait_for('message', check=check2, timeout=120.0)
        except asyncio.TimeoutError:
            await author.send("I can't wait forever, "
                                        "try again when ready")
            self.settings[server.id]['usercache'].remove(author.id)
            self.save_json()
            bool = False

        if bool == True:
            await self.send_suggest(message, server)
            await author.send("Your suggestion was submitted.")

    async def send_suggest(self, message, server):

        author = server.get_member(message.author.id)
        suggestion = message.clean_content
        avatar = author.avatar_url if author.avatar \
            else author.default_avatar_url

        em = discord.Embed(title="Suggestion Ticket Raised!", color= discord.Color.purple())
        em.set_author(name=author.display_name ,icon_url=avatar)
        em = em.add_field(name="-----", value="<:MB:400665334882762762> - Support Request raised by {0.display_name}".format(author), inline=False)
        em = em.add_field(name="-----", value=":timer: - **{0}**".format(time.strftime("%Y.%m.%d %H:%M")), inline=False)
        em = em.add_field(name="-----", value=":notepad_spiral: - Suggestion Report:\n  _{}_".format(suggestion), inline=False)

        for output in self.settings[server.id]['output']:
            where = server.get_channel(output)
            if where is not None:
                await where.send(embed=em)

        self.settings[server.id]['usercache'].remove(author.id)
        self.save_json()