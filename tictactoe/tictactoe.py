import discord
import asyncio
import random
import textwrap
 
# X is player 1
# O is player 2
# whoever invokes the tictactoe command is X
# their opponent is O
#
# each cell here is a bit in a 9 bit uint
#              84
#              /
# ┌───┬───┬───┐
# │  1│  2│  4│ - 7
# ├───┼───┼───┤
# │  8│ 16│ 32│ - 56
# ├───┼───┼───┤
# │ 64│128│256│ - 448
# └───┴───┴───┘
#   |   |   |  \
#  73 146 292  273
#
# each player has a "score", which is a sum of the cells they
# have marked as theirs. checking for wins then becomes checking
# this 9 bit uint for certain values, which represents how many, and
# what cells a player has filled up.

    async def tictactoe(self, ctx, opponent : discord.Member=None):
        WINNING_STATES = [7, 56, 448, 73, 146, 292, 84, 273]
        monospaced = "```\n{}\n```"
         
        if opponent is None:

 
        moves = 0
        ch = ctx.message.channel
        cells = [[256, 0], [128, 0], [64, 0], [32, 0], [16, 0], [8, 0], [4, 0], [2, 0], [1, 0]]
        players = {"X": ctx.message.author, "O": opponent}
        score = {"X": 0, "O": 0}
        turn = "X"
 
        def win(score):
            for state in WINNING_STATES:
                if state & score == state:
                    return True
            return False
 
        def display_board(winner=None):
            final_msg = """
                ┌─┬─┬─┐
                │{0[0]}│{0[1]}│{0[2]}│
                ├─┼─┼─┤
                │{0[3]}│{0[4]}│{0[5]}│
                ├─┼─┼─┤
                │{0[6]}│{0[7]}│{0[8]}│
                └─┴─┴─┘
                X: {1}
                O: {2}
                {3}
            """
            final_msg = textwrap.dedent(final_msg)
            board = ["X" if sq[1] == 1 else "O" if sq[1] == 2 else " " for sq in cells]
            if winner:
                if winner in ["X", "O"]:
                    msg = "{} wins!".format(players[winner].name)
                else:
                    msg = winner
            else:
                msg = "It's {}'s turn. Send a number between 1 and 9 to make a move.".format(players[turn].name)
            return final_msg.format(board, players["X"].name, players["O"].name, msg)
 

                # right now, just pick a random cell that's not filled
                # later on a better AI could be made or whatever
                while True:
                    move = random.randint(0, 8)
                    if cells[move][1] != 0:
                        continue
                    else:
                        cell = move
                        break
            else:

 
                if msg.content.lower() in ["quit", "abort", "stop", "exit"]:
                    # because why not
                    if msg.author in players.values():

                elif not msg.content.isdigit():
                    continue
 
                cell = int(msg.content) - 1
                if cell < 0 or cell > 8:

                    continue
 
            moves += 1
            score[turn] += cells[cell][0]
            cells[cell][1] = 1 if turn == "X" else 2
            if win(score[turn]):

