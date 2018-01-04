import discord
from discord.ext import commands
from random import randint

class Battleship:

    @commands.command(pass_context=True)
    async def battleship(self, ctx):

        #----------------------------------------------------------------# 
        num = 0
        num2 = 0
        num3 = 0
        msg = ""
        msg2 = ""
        total = 0
        turn = 10
        turn2 = 0
        check = 0
        loop = True
        embedPrint = 0
        error = "Error. Invalid Response."

        miss = "You missed my battleship!"
        hit1 = "You sunk part of a battleship!"
        hit2 = "You sunk a battleship!"
        ocean = "Oops, that's not even in the ocean."
        guess = "You already guessed that one."
        over = 'Game Over'
        
        reply2 = ""
        reply = ""
        shipM = ""
        shipP = ""
        board = []
        seperate = []
        author = ctx.message.author
        channel = ctx.message.channel



        embed=discord.Embed(
            title="About Battleship", 
            description="~ A simple game of Battle Ships built into Magik Bot.\n:black_circle: - Open Target\n:red_circle: - Missed Target\n:large_blue_circle: = Target Hit\n⚪ = Location of ships (at the end of the game)", 
            color=0x207cee)
        embed.set_author(
            name="Magik bot", url='http://www.magikbot.co.uk', 
            icon_url='https://cdn.discordapp.com/attachments/355249562719617024/357107055691169797/MB_Icon.png')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/355249562719617024/365100412874784768/Battleship-ubicom-VIDEO-launch_trailer_2016_08_02-712x712_Desktop_261122.png')
        embed.add_field(
            name="How to play", 
            value="Enter your X and Y value as a comment like this `4 2`. No prefix required. Type `cancel` to stop the game.", 
            inline=True)
        embed.add_field(
            name="How many turns", 
            value="You have 9 attempts to hit my 4 ships", 
            inline=True)
        embed.add_field(
            name="Author", 
            value="UnseenMagik & Dp", 
            inline=True)
        embed.add_field(
            name="Battleship Board Layout",
            value=("```Y   1 O O O O O\n"
                   "    2 O O O O O\n"
                   "A   3 O O O O O\n"
                   "X   4 O O O O O\n"
                   "I   5 O O O O O\n"
                   "S   0 1 2 3 4 5\n"
                   "    X   A X I S```"), inline=True)
        embed.set_footer(
            text="Magik Bot - Providing Discord support since September 2017")
        
        await ctx.send(embed=embed) 
        




        """
            10 9 8 7 6 5 4 3 2 1
        Y    O O O O O O O O O O  10
             O O O O O O O O O O  9
        A    O O O O O O O O O O  8
        X    O O O O O O O O O O  7
        I    O O O O O O O O O O  6
        s    O O O O O O O O O O  5
             O O O O O O O O O O  4
             O O O O O O O O O O  3
             O O O O O O O O O O  2
             O O O O O O O O O O  1
            X Axis
        """

        for x in range(5): #Size of the board
            board.append([":black_circle:"] * 5)

        def print_board(board): #Making the board
            i = "\n"
            for x in board:
                i = i + " ".join(x)+"\n"
                #print(len(x))
            i += ""
            return i
        
        



        print ("Let's play Battleship!")
        print (" ")
        await ctx.send("Let's play Battleship!"+ "\n")
 
        

        def random_x(board):
            return randint(0, len(board) - 1)

        def random_y(board):
            return randint(0, len(board) - 1)

        #ship(num)a is equal to x
        #ship(num)b is equal to y
        #ship(num)c is equal to new x
        #ship(num)d is equal to new y

        ship_x = random_x(board)
        ship_y = random_y(board)

        ship1a = random_x(board)#X
        ship1b = random_y(board) #Y
        #ship1c = New Y
        #Vertical Ships

        if ship1a == 0:
            ship1d = ship1a + 1
        elif ship1a == 4:
            ship1d = ship1a - 1
        else:
            ship1d = ship1a + 1


        ship2a = random_x(board) #X
        ship2b = random_y(board) #Y
        #ship2c = New X
        #Horizontal Ships

        if ship2b == 0:
            ship2c = ship2b + 1
            
        elif ship2b == 4:
            ship2c = ship2b - 1
            
        else:
            ship2c = ship2b + 1

        l = len(board)
        
        #For debugging purposes
        print("Ship 1: ", ship_x+1, ship_y+1)
        print("Ship 2: ", ship1a+1, ship1b, " ", ship1d+1, ship1b)
        print("Ship 3: ", ship2a+1, ship2b, " ", ship2a+1, ship2c)


        def embed_board(turn2):
            embed=discord.Embed(
                title="The Board",
                description=" ",)
            embed.add_field(
                name="Turn "+str(turn2),
                value=print_board(board),
                inline=True)
            reply = embed
            return embed
 
        while turn != 0:


            #for turn in range(10):
            reply2 = ""
            """embed=discord.Embed(
                title="The Board",
                description=" ",)
            embed.add_field(
                name="Current Board ",
                value=print_board(board),
                inline=True)"""
            #reply = embed
            reply = embed_board(turn2)
            check += 1
            print("Turns:"+str(turn))

            #Send Embed here, edit later#
            if embedPrint == 0:
                message_Embed = await ctx.send(embed=reply)

            else:
                await ctx.edit_message(message_Embed, embed=reply)

            guess_x = -1
            guess_y = -1
            #await ctx.send_typing(channel)
            guessing = await ctx.send("\n"+"Guess X and Y:")                
            msg = await self.bot.wait_for_message(timeout=30,author=author, channel=channel)
            await ctx.delete_message(guessing)

            if msg.content == "Cancel" or msg.content == "cancel":
                await ctx.send("Stopping game.")
                print("Stopping the game.")
                #loop = False
                break
            #Catches any errors, such as bad input. Not numbers, not 2 answers, etc.
            try:
                msg2 = msg.content
                seperate = msg2.split(" ")

                guess_x = int(seperate[1]) - 1 
                guess_y = int(seperate[0]) - 1

            except IndexError:
                reply2 = error
                print("Invalid Response. IndexError")
                turn += 1
                turn2 -= 1
                    
            except ValueError:
                turn += 1
                turn2 -= 1
                reply2 = error
                print("Invalid Response. ValueError")
                    
            except UnboundLocalError:
                turn += 1
                turn2 -= 1
                reply2 = error
                print("Invalid. UnboundLocalError")
                
            #Deletes users answer, like 1 3. Needs proper perms though.   
            try:
                await self.bot.delete_message(msg)
                    
            except discord.errors.Forbidden:
                print('discord.errors.Forbidden')
                await ctx.send('Error. Don\'t have the permissions. Stopping game.')
                #loop = False
                break
                
            if total == 4:
                await ctx.send("You sunk all the ships!")
                print("All ships sunk.")
                    
                if total == 4:
                    await ctx.send("You hit em all captain.\n Game Over.")
                    await ctx.edit_message(message_Embed, embed=reply)
                    #loop = False
                        
                break
                
            elif guess_x == ship_x and guess_y == ship_y:
                board[guess_x][guess_y] = ":large_blue_circle:"
                print("Sunk a ship.")
                reply2 = hit2
                total += 1

            #-------------------------------------------#    
            elif guess_x == ship1a and guess_y == ship1b:
                board[guess_x][guess_y] = ":large_blue_circle:"
                if num == 0:
                    print("Part of ship sunk.")
                    reply2 = hit1
                    num += 1

                else:
                    print("You sunk a battleship.")
                    reply2 = hit2
                        
                total += 1 

            elif guess_x == ship1d and guess_y == ship1b:

                board[guess_x][guess_y] = ":large_blue_circle:"

                if num == 0:
                    print("You sunk part of a battleship!")
                    reply2 = hit1
                    num += 1

                else:
                    print("You sunk a battleship.")
                    reply2 = hit2
                        
                total += 1
                #-----------------------------------------------#
            elif guess_x == ship2a and guess_y == ship2b:

                board[guess_x][guess_y] = ":large_blue_circle:"

                if num2 == 0:
                    reply2 = hit1
                    print("You sunk part of a battleship!")
                    num2 += 1

                else:
                    reply2 = hit2
                    print("You sunk a battleship.")
        
                total += 1

            elif guess_x == ship2a and guess_y == ship2c:

                board[guess_x][guess_y] = ":large_blue_circle:"

                if num2 == 0:
                    reply2 = hit1
                    print("You sunk part of a battleship!")
                    num2 += 1

                else:
                    reply2 = hit2
                    print("You sunk a battleship.")

                total += 1
                #--------------------------------------#
                


            else:
                if (guess_x < 0 or guess_x > l-1) or (guess_y < 0 or guess_y > l-1):
                    reply2 = ocean
                    print ("Oops, that's not even in the ocean.")
                        
                elif(board[guess_x][guess_y] == ":red_circle:"):
                    reply2 = guess
                    turn += 1
                    print ("You guessed that one already.")
                        
                else:
                    print ("You missed my battleship!")
                    board[guess_x][guess_y] = ":red_circle:"
                    reply2 = miss

                    """if turn <= 0:
                        reply2 = over
                        print ("Game Over")
                            
                        board[ship_x][ship_y] = ":white_circle:"
                        board[ship1d][ship1b] = ":white_circle:" 
                        board[ship1a][ship1b] = ":white_circle:"
                        board[ship2a][ship2b] = ":white_circle:"
                        board[ship2a][ship2c] = ":white_circle:"
                            
                        await self.bot.edit_message(message_Embed, embed=reply)
                        print(" ")
                        print("Here are all the ships, they're labeled M.")
                        break
                        #loop = False"""         

            if embedPrint == 0:
                shipM = await ctx.send(reply2)
            else:
                await ctx.edit_message(shipM, reply2)
            embedPrint += 1
            turn -= 1
            turn2 += 1

        #reply2 = over
        print ("Game Over")
                            
        board[ship_x][ship_y] = ":white_circle:"
        board[ship1d][ship1b] = ":white_circle:" 
        board[ship1a][ship1b] = ":white_circle:"
        board[ship2a][ship2b] = ":white_circle:"
        board[ship2a][ship2c] = ":white_circle:"
        reply = embed_board(turn2)                    
        await ctx.edit_message(message_Embed, embed=reply)
        await ctx.send(over)
        print(" ")
        print("Here are all the ships, they're labeled M.")


            #----------------------------------------------------------------#
