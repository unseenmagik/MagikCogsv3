from discord.ext import commands
from .dataIO import dataIO
import discord
import os
import asyncio
import datetime
from redbot.core.json_io import JsonIO
from pathlib import Path
import sqlite3

dir = os.getcwd()
config_dir = Path(dir)
config_dir.mkdir(parents=True, exist_ok=True)
g = config_dir / 'data/counter/count.json'
f = config_dir /'data/counter/count.db'
db = sqlite3.connect(str(f))
c = db.cursor()

class Counter:
    '''Check when someone was last seen.'''
    def __init__(self, bot):
        self.bot = bot

        db.execute("CREATE TABLE IF NOT EXISTS Count(ID TEXT, Counter REAL)")
        """self.data = {
            "Author": 'Ping',
            "Counter": 0
        }
        self.messages = {
            "Author": 'Ping',
            "Counter": 0
        }#JsonIO(g)._load_json()
        print(self.messages)"""
        #self.seen = dataIO.load_json('data/seen/seen.json')
        self.new_data = False



    async def data_writer(self):
        print('ping')
        while self == self.bot.get_cog('Counter'):
            if self.new_data:
                #print(self.seen)

                dataIO.save_json('data/Counter/count.json', self.seen)
                self.new_data = False
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(30)
    async def listener(self, message):
        #print("Listener")
        ID = str(message.author.id)
        counter = 1
        selector = 'Counter'
        data = c.execute('SELECT * FROM Count')
        #[print(row) for row in c.fetchall()]
        c.execute('SELECT ID FROM Count ')
        IDs = c.fetchall()
        #print(IDs)
        #print(ID)
        if str(ID) in str(IDs):
            print("Same ID")
            c.execute('SELECT {1} FROM Count WHERE ID={0}'.format(ID, selector))
            counter2 = c.fetchall()
            count = str(counter2[0])
            count = count.replace(",", "")
            count = count.replace(".0", "")
            count = count.replace("(", "")
            count = count.replace(")", "")
            count = int(count)
            #print(count)
            #count = int(count)
            counter3 = count + 1
            #print(counter3)
            #counter = counter + 1
            c.execute('UPDATE Count SET Counter = {} WHERE ID ={}'.format(counter3, ID))
            db.commit()
            #sql = 'SELECT Counter FROM Count WHERE ID=?'
            #result = c.execute(sql, ID)
            #print(result)
        else:
            print("New ID")
            #print(data)

            #if ID in data:
            c.execute("INSERT INTO Count (ID, Counter) VALUES (?, ?)", (ID, counter))
            db.commit()

        """data = self.messages
        #print("First Count: ", data["Counter"])
        #counter = 0
        author2 = data["Author"]
        if author2 in data["Author"]:
            counter = data["Counter"]
            counter += 1
        if data["Counter"] == 0:
            counter = 1
        else:
            counter = data["Counter"]
            counter += 1
        #data = {}
        #print("After Count: ",counter)
        data["Author"] = message.author.display_name + ":" + str(message.author.id)
        data["Counter"] = counter"""
        """#[18:]
        bool = False
        file2 = open(f, "r")
        inte = 0
        string3 = ""
        for line in file2:
            if str(message.author.id) in line:
                string = str(line) #+ str(1)
                string2 = str(line)
                string2 = string2[20:22]
                #string2 = string2.replace("'", "")
                #string2 = string2.replace(")", "")
                inte = int(string2)
                print("Before: ", inte)
                inte += 1
                print("After: ", inte)
                string3 = "{} : {}".format(string[:18], inte)
                print("String 3:", string3)
                #file2 = open(f, "w")
                #file2.write(string3)
                #file2.close()
                bool = True

        if bool == True:
            file3 = open(f, "r")
            lines = open(f).read().splitlines()
            print(lines)
            num_lines = sum(1 for line in open(f))
            print("Num lines: ",num_lines)
            #dat = open(f).read().splitlines()
            for line in file3:
                #for i in range(50):
                for i in range(num_lines):
                    if str(message.author.id) in line:
                        #string4 = line + string3
                        #print("Inte: ",inte)

                        #print("String 4: ", string4)
                        #print(i)
                        #lines[i] = str(string3)
                        #line[i] = "\n"
                        lines[i] = "\n{}".format(string3)
                        #lines = lines[:2]
                        print("String 3: ", string3)
                        print("Lines I: ", lines[i])
                        print("Lines: ",lines)
                print(lines)
                open(f, "w").write(''.join(lines))
                return print("Done")
            #with open(f, "w") as  file4:
                #file4.writelines(file3)
            file3.close()
        else:
            #counter = 0
            data2 = "{} : {}".format(message.author.id, inte)#str(message.author.id) ," ",str(inte)
            #self.messages = data
            print("Data 2: ",data2)
            file = open(f, 'a')
            file.write(str(data2) +"\n")
            file.close()
            #file = open(f, "r")
            #print (file.read())"""
        """author = message.author
            self.data = data
            #self.data = on_msg(self, message)
            print(self.data)
            data2 = {}
            data2.update(self.messages)
            data2.update(data)
            print(data2)
            self.messages = data2
            #self.messages = self.messages.update(data)
            print(self.messages)"""
            #JsonIO(g)._save_json(self.messages)



    @commands.command(pass_context=True, no_pm=True, name='msg')
    async def _seen(self, context):
    #async def _seen(self, context, username: discord.Member):
        '''seen <@username>'''
        print("Command")
        channel = context.message.channel
        with open(f, "rb") as q:
            await context.send(file=discord.File(q))
        #await context.send(file=discord.File(f))
        #await context.send(self.messages)
        #print(context.message)
        #Msg = context.message
        server = context.message.guild
        #author = username
        timestamp_now = datetime.datetime.now()
        #print(timestamp_now)
        
        #Change "server.id" to "guild.id"
        """if server.id in self.seen:
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
            await context.send('{}'.format(message))"""

    async def on_msg(self, message):
        print("On message")
        #Change this from new update of discord py
        author = message.author
        data = {}
        data['Author'] = author
        self.message = author
        channel = message.channel
        await channel.send("Message recorded")

        """if self.bot.user.id != message.author.id:
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
            self.new_data = True"""