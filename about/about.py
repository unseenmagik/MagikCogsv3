from discord.ext import commands

class About:
    """More information about Magik Bot"""
    
    @commands.command()
    @checks.admin_or_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason: str=None):
        await ctx.guild.ban(user)
        case = modlog.create_case(
            ctx.guild, ctx.message.created_at, "ban", user,
            ctx.author, reason, until=None, channel=None
        )
        await ctx.send("Done. It was about time.")
       
