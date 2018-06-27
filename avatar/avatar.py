
from random import choice, randint
import random
import aiohttp
import discord
import asyncio
from discord.ext import commands
from redbot.core import checks, bank
from redbot.core.utils.chat_formatting import pagify, box
from redbot.core.data_manager import bundled_data_path
from redbot.core.data_manager import cog_data_path
from .data import links, messages
import datetime
import os
import string
import time
import io
from redbot.core.i18n import Translator
from redbot.core.utils.chat_formatting import pagify, box

class Avatar():
    """Cog for pulling a users avatar into a .png file"""

    @commands.command(pass_context=True)
    async def avatar(self, ctx, member:discord.Member=None):
        async with ctx.channel.typing():
            if member is None:
                member = ctx.message.author
            if member.is_avatar_animated():
                async with self.session.get(member.avatar_url_as(format="gif")) as resp:
                    data = await resp.read()
                file = discord.File(io.BytesIO(data),filename="{}.gif".format(member.name))
            if not member.is_avatar_animated():
                async with self.session.get(member.avatar_url_as(static_format="png")) as resp:
                    data = await resp.read()
                file = discord.File(io.BytesIO(data),filename="{}.png".format(member.name))
            await ctx.send(file=file)
