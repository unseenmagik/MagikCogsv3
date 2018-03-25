from discord.ext import commands
from .dataIO import dataIO
import discord
import os
import asyncio
import datetime





class Seen:
    '''Check when someone was last seen.'''
    def __init__(self, bot):
        self.bot = bot
        self.seen = dataIO.load_json('data/seen/seen.json')
        self.new_data = False

    async def data_writer(self):
        #print('ping')
        while self == self.bot.get_cog('Seen'):
            if self.new_data:
                #print(self.seen)
                dataIO.save_json('data/seen/seen.json', self.seen)
                self.new_data = False
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(30)

    @commands.command(pass_context=True, no_pm=True, name='seen')
    async def _seen(self, context, username: discord.Member):
        '''seen <@username>'''
        #print(context.message)
        #Msg = context.message
        server = context.message.guild
        author = username
        timestamp_now = datetime.datetime.now()
        #print(timestamp_now)
        
        #Change "server.id" to "guild.id"
        if server.id in self.seen:
            if author.id in self.seen[server.id]:
                data = self.seen[server.id][author.id]
                timestamp_then = datetime.datetime.fromtimestamp(data['TIMESTAMP'])
                #print(timestamp_then)
                timestamp = timestamp_now - timestamp_then
                days = timestamp.days
                seconds = timestamp.seconds
                hours = seconds // 3600
                seconds = seconds - (hours * 3600)
                minutes = seconds // 60
                if sum([days, hours, minutes]) < 1:
                    ts = 'just now'
                else:
                    ts = ''
                    if days == 1:
                        ts += '{} day, '.format(days)
                    elif days > 1:
                        ts += '{} days, '.format(days)
                    if hours == 1:
                        ts += '{} hour, '.format(hours)
                    elif hours > 1:
                        ts += '{} hours, '.format(hours)
                    if minutes == 1:
                        ts += '{} minute ago'.format(minutes)
                    elif minutes > 1:
                        ts += '{} minutes ago'.format(minutes)
                em = discord.Embed(color=discord.Color.green())
                avatar = author.avatar_url if author.avatar else author.default_avatar_url
                em.set_author(name='{} was seen {}'.format(author.display_name, ts), icon_url=avatar)
                await context.send(embed=em)
            else:
                message = 'I haven\'t seen {} yet.'.format(author.display_name)
                await context.send('{}'.format(message))
        else:
            message = 'I haven\'t seen {} yet.'.format(author.display_name)
            await context.send('{}'.format(message))

    async def on_message(self, message):
        #Change this from new update of discord py

        if self.bot.user.id != message.author.id:
            #if not any(message.content.startswith(n) for n in self.bot.settings.prefixes):
            server = message.guild
            author = message.author
            ts = datetime.datetime.now().timestamp()
            #ts = datetime.datetime.now().strftime('%H:%M:%S')
            #ts = message.timestamp.timestamp()
            data = {}
            data['TIMESTAMP'] = ts
            if server.id not in self.seen:
                self.seen[server.id] = {}
            self.seen[server.id][author.id] = data
            self.new_data = True


