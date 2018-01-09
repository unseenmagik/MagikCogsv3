import discord
import os
import os.path
import json
from .utils import checks
from .utils.dataIO import dataIO
from discord.ext import commands

class Say:
    """Make your bot say or upload something in the channel you want.
    
    Report a bug or ask a question: https://discord.gg/WsTGeQ"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json('data/say/settings.json')

    @commands.group(pass_context=True)
    async def send(self, ctx): # Had to choose something else than say :c have a better idea ?
        if ctx.invoked_subcommand is None:
            pages = self.bot.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await self.bot.send_message(ctx.message.channel, page)

    @send.command(pass_context=True)
    async def here(self, ctx, *, text):
        """Say a message in the actual channel"""
        
        message = ctx.message
        server = message.guild
        
        if server.id not in self.settings:
            self.settings[server.id] = {'autodelete': '0'}

        if self.settings[server.id]['autodelete'] == '1':
            await self.bot.delete_message(message)

        else:
            pass

        await self.bot.say(text)

            
    @send.command(pass_context=True)
    async def channel(self, ctx, channel : discord.Channel, *, text):
        """Say a message in the chosen channel"""

        message = ctx.message
        server = message.server
        
        if server.id not in self.settings:
            self.settings[server.id] = {'autodelete': '0'}

        if self.settings[server.id]['autodelete'] == '0' or server.id not in self.settings:
            pass
        
        else:
            await self.bot.delete_message(message)

        await self.bot.send_message(channel, text)

    
    @checks.serverowner_or_permissions(administrator=True)
    @send.command(pass_context=True)
    async def autodelete(self, ctx):
        """Enable the auto-deletion of the message that invoked the command.
            
        If your bot is fast enough, users won't see at all the message with the command, useful to talk as your bot with long conversations"""
            
        server = ctx.message.server
        
        if server.id not in self.settings:
            self.settings[server.id] = {'autodelete': '0'}
        
        if not ctx.message.channel.permissions_for(ctx.message.server.me).manage_messages:
            await self.bot.say("Error: I need the `Manage messages` permission to enable this function. Aborting...")
            return
        else:
            pass
        
        if self.settings[server.id]['autodelete'] == '0':
            self.settings[server.id]['autodelete'] = '1'
            await self.bot.say("Auto-deletion is now enabled. Note that this will only work on commands of these cog. For further options,look at `" + ctx.prefix + "modset deleterepeat`")

        else:
            self.settings[server.id]['autodelete'] = '0'
            await self.bot.say("Auto-deletion is now disabled")

        dataIO.save_json('data/say/settings.json', self.settings)

