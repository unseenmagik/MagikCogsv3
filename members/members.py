import discord
from discord.ext import commands
from redbot.core import checks

class Members:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @checks.admin_or_permissions(administrator=True)
    async def smembers(self, ctx):
        """Get members via names, count, etc."""
        prefix = ctx.prefix
        msg = ctx.message.content
        print(msg)
        msg = msg[7:]
        print(msg)
        em = discord.Embed(
            title="Subcommands",
            description="Here are the sub commands for 'smembers'",
            color=discord.Color.blue()
        )
        em.add_field(
            name="**all**",
            value="Get all members in the server\nExample: ``{}smembers all``".format(prefix),
            inline=False
        )
        em.add_field(
            name="**total**",
            value="Check the total amount of members in your guild!\nExample: ``{}smembers total`` to list total".format(prefix)
        )
        em.add_field(
            name="**search**",
            value="Search through multiple parameters. Type ``{}smembers search`` for more information.".format(prefix)
        )
        if msg == "s":

            await ctx.send(embed=em)
        elif msg == "s search":
            # Error, no params given. Show sub commands
            em = discord.Embed(
                title="Subcommands for **search**",
                description="Below are the subcommands for **search**",
                color=discord.Color.dark_blue()
            )
            em.add_field(
                name="**role**",
                value="Find all members in a specific role.\nExample: ``{}smembers search role <role>``".format(prefix),
                inline=False
            )
            em.add_field(
                name="**name**",
                value="Find all members with a similar name.\nExample: ``{}members search name <name>``".format(prefix),
                inline=False
            )
            em.add_field(
                name="**ID**",
                value="Find a specific person with an ID.\nExample: ``{}smembers search ID <ID>``".format(prefix),
                inline=False
            )
            await ctx.send(embed=em)

    #Search for a ID or a name
    @members.command(pass_context=True)
    async def search(self, ctx, *, message):
        guild = ctx.guild
        prefix = ctx.prefix
        my_List = []
        List = []
        total = 0
        num2 = 0
        number = 0
        Message = ""
        num = 0
        def get_members(self, ctx, number, message):
            guild = ctx.guild
            msg = " "
            temp = ""
            my_List = []

            if number == 2:
                message = message[4:]
                temp = temp + str(message)
                temp = temp[1:]
                temp = temp.lower()
                print("Temp:\n", temp)
            elif number == 3:
                message = message[3:]
            for member in guild.members:
                if number == 1:
                    for roles in member.roles:
                        if str(roles) in message:
                            msg = "**" + str(member.name) + "#" + str(member.discriminator) + "** - " + str(member.id) + "\n" + "\n"
                            my_List.append(msg)
                elif number == 2:
                    print(member.display_name)
                    memberName = str(member.display_name)
                    memberName = memberName.lower()

                    if temp in memberName:
                        #print("Blep")
                        msg = "**{}#{}** - {}\n".format(member.name, member.discriminator, member.id)
                        my_List.append(msg)
                elif number == 3:

                    print(member.id)
                    print(message)
                    if str(member.id) == str(message):
                    #if str(message == str(member.id):
                        msg = "**{}#{}** - {}\n".format(member.name, member.discriminator, member.id)
                        my_List.append(msg)
                elif number == 4:
                    msg = "**{}#{}** - {}\n".format(member.name, member.discriminator, member.id)
                    my_List.append(msg)

            my_List.sort()
            return my_List

        def print_total_members(self, ctx, my_List):
            total = 0
            Message = " "
            num2 = 0

            for i in my_List:
                leng = len(i)
                leng = leng + num2
                num2 = 0
                total += leng
                if total > 2000:
                    Message = Message + "|" + str(i)
                    total = 0
                    num2 = leng
                else:
                    Message = Message + str(i)
            return Message

        async def get_total(self, ctx):
            guild = ctx.guild
            num = 0
            for member in guild.members:
                num += 1
            return num
        def get_role_total(self, ctx, role):
            guild = ctx.guild
            num = 0
            for member in guild.members:
                for roles in member.roles:

                    if str(roles.name) in role:
                        num += 1
            return num

        #Search commands: role, name, ID.
        if "role" in message:
            role = message[5:]
            role_total = get_role_total(self, ctx, role)
            #Search roles, 1
            number = 1

        elif "name" in message:
            #Search by name, 2
            number = 2

        elif "ID" in message:
            #Search by ID, 3
            number = 3
        #Add "all"?
        elif "all" in message:
            number == 4

        else:
            #Error, no params given. Show sub commands
            em = discord.Embed(
                title="Subcommands for **search**",
                description="Below are the subcommands for **search**",
                color=discord.Color.dark_blue()
            )
            em.add_field(
                name="**role**",
                value="Find all members in a specific role.\nExample: ``{}smembers search role <role>``".format(prefix),
                inline=False
            )
            em.add_field(
                name="**name**",
                value="Find all members with a similar name.\nExample: ``{}smembers search name <name>``".format(prefix),
                inline=False
            )
            em.add_field(
                name="**ID**",
                value="Find a specific person with an ID.\nExample: ``{}smembers search ID <ID>``".format(prefix),
                inline=False
            )
            await ctx.send(embed=em)
        if number == 1:
            my_List = get_members(self, ctx, number, message)
            send = print_total_members(self, ctx, my_List)
            if len(send) > 2000:

                List = send.split("|")
            else:
                send = send
            if len(List) >= 1:
                for f in List:
                    print(len(f))
                    print(f)
                    await ctx.send(f)
            else:
                await ctx.send(send)
            pass
            await ctx.send("Total members in the {} role: **{}**".format(role, role_total))

        elif number == 2:
            my_List = get_members(self, ctx, number, message)
            send = print_total_members(self, ctx, my_List)
            print("Send: ", send)
            if len(send) > 2000:

                List = send.split("|")
            else:
                send = send
            if len(List) >= 1:
                for f in List:
                    print(len(f))
                    print(f)
                    await ctx.send(f)
            else:
                try:
                    await ctx.send(send)
                except:
                    await ctx.send("Found nobody with that matches your search.")
            pass

        elif number == 3:
            my_List = get_members(self, ctx, number, message)
            await ctx.send(print_total_members(self, ctx, my_List))

        elif number == 4:
            my_List = get_members(self, ctx, number, message)
            await ctx.send(print_total_members(self, ctx, my_List))
            await ctx.send("Total members in the {} role: **{}**".format(role, role_total))

    #Get all members
    #Put this with search, [p]smembers search all ?
    @members.command(pass_context=True)
    async def all(self, ctx):
        guild = ctx.guild
        my_List = []
        List = []
        total = 0
        num2 = 0
        Message = ""
        num = 0

        #if message == "all":
        for member in guild.members:
            msg = "**{}#{}** - {}\n".format(member.name, member.discriminator, member.id)
            #msg = "**"+str(member.name) + "#" + str(member.discriminator) + "** - " + str(member.id) + "\n" + "\n"
            my_List.append(msg)
            num += 1
        my_List.sort()
        for i in my_List:
            leng = len(i)
            leng = leng + num2
            num2 = 0
            total += leng
            if total > 2000:
                Message = Message + "|" + str(i)
                total = 0
                num2 = leng
            else:
                Message = Message + str(i)
        if len(Message) > 2000:
            List = Message.split("|")
        else:
            send = Message
        if len(List) >= 1:
            for f in List:
                print(len(f))
                print(f)
                await ctx.send(f)
        else:
            await ctx.send(send)
        await ctx.send("Total members in this guild: **{}**".format(num))

    #Get total number of members ONLY
    @members.command(pass_context=True)
    async def total(self, ctx):
        guild = ctx.guild
        num = 0
        for member in guild.members:
            num += 1
        await ctx.send("Total members in this guild: **{}**".format(num))
