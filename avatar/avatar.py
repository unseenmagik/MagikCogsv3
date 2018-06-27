from discord.ext import commands
import discord

class Avatar:
    """View a users avatar"""

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
