import discord
from discord.ext import commands

class Say:
    """Make your bot say something in the channel you want."""


    @commands.command(pass_context=True)
    async def send(self, ctx): 
        """This does stuff!"""
        # Your code will go here
        #Will focus on here later on, should manually input the help than using self.
        if ctx.invoked_subcommand is None
            pages = self.bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            await ctx.send(ctx.message.channel, page)
           
        
    @send.command(pass_context=True)
    async def here(self, ctx, *, text):
        """Say a message in the actual channel"""
        
        message = ctx.message
        server = message.guild
        
        #Remove this because we would always want your message to auto delete
        """if server.id not in self.settings:
            self.settings[server.id] = {'autodelete': '0'}

        if self.settings[server.id]['autodelete'] == '1':
            await self.bot.delete_message(message)

        else:
            pass"""
        try:
            await self.bot.delete_message(message)
        except Forbidden:
            print("Unable to delete Users message. Proceeding...")
        await self.bot.say(text)

            
    @send.command(pass_context=True)
    async def channel(self, ctx, channel : discord.Channel, *, text):
        """Say a message in the chosen channel"""

        message = ctx.message
        server = message.guild
        
        #Same thing as above
        """if server.id not in self.settings:
            self.settings[server.id] = {'autodelete': '0'}

        if self.settings[server.id]['autodelete'] == '0' or server.id not in self.settings:
            pass
        
        else:
            await self.bot.delete_message(message)"""
        try:
            await self.bot.delete_message(message)
        except Forbidden:
            print("Unable to delete Users message. Proceeding...")
        await self.bot.say(text)




