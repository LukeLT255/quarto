from collections import namedtuple
from games import (Game)
from queue import PriorityQueue
from copy import deepcopy
import numpy as np


pieces = [0b0000, 0b0001, 0b0010, 0b0011, 0b0100, 0b0101, 0b0110, 0b0111, 0b1000, 0b1001, 0b1010,
          0b1011, 0b1100, 0b1101, 0b1110, 0b1111,]




class TemplateState:    # one way to define the state of a minimal game.

    def __init__(self, player, board, piecesAvailable, pieceToBePlaced, pieceChosenForOpponent, label=None, depth=8): # add parameters as needed.
        self.to_move = player
        self.board = board
        self.maxDepth = depth
        self.label = label
        self.piecesAvailable = piecesAvailable
        self.pieceToBePlaced = pieceToBePlaced
        self.pieceChosenForOpponent = pieceChosenForOpponent
        # add code and self.variables as needed.

    def __str__(self):  # use this exact signature
        return self.label

    # class TemplateAction:
    #     '''
    #     It is not necessary to define an action.
    #     Start with actions as simple as a label (e.g., 'Down')
    #     or a pair of coordinates (e.g., (1,2)).
    #
    #     Don't un-comment this until you already have a working game,
    #     and want to play smarter.
    #     '''
    #     def __lt__(self, other):    # use this exact signature
    #         # return True when self is a better move than other.
    #         return False


class TemplateGame(Game):
    '''
    This is a minimal Game definition,
    the shortest implementation I could run without errors.
    '''
    # h and v define size of board, k defines how many needed in a row to win.
    def __init__(self, initial, h=4, v=4, k=4):    # add parameters if needed.
        self.initial = initial
        self.h = h
        self.v = v
        self.k = k
        self.initial = TemplateState(player='Player1', board={}, piecesAvailable={}, pieceToBePlaced={}, pieceChosenForOpponent={} )

        # add code and self.variables if needed.






    def actions(self, state):
        if state.pieceChosenForOpponent == None: #returns open spaces on the board if player has not yet placed given game piece
            try:
                return state.moves
            except:

                    pass
                    "Legal moves are any square not yet taken"
                    moves = []
                    for x in range(1, self.h + 1):
                        for y in range(1, self.v + 1):
                            if (x, y) not in state.board.keys():
                                moves.append((x, y))
                    state.moves = moves
                    state.pieceChosenForOpponent = "" #changing value of this var to move on to next block of code next move

                    return moves

        else: #returns pieces to give to opponent
            try:
                return state.moves

            except:
                pass
                moves = []
                for x in state.piecesAvailable:
                    moves.append(x)
                state.moves = moves
                state.pieceChosenForOpponent = "selected"  #changes piecesChosenForOpponent to switch opponents
                return moves



    def opponent(self, player, state):
        if player == 'Player1' and state.pieceChosenForOpponent == "selected": #If player1 has placed piece and chosen for opponent then switch players
            state.pieceChosenForOpponent = None #resets piece chosen for opponent
            return 'Player2'
        if player == 'Player2' and state.pieceChosenForOpponent == "selected": #If player2 has placed piece and chosen for opponent then switch players
            state.pieceChosenForOpponent = None #resets piece chosen for opponent
            return 'Player1'
        if player == 'Player1' and not state.pieceChosenForOpponent == "":   #If player 1 has placed piece, but not selected opponents piece
            return 'Player1'
        if player == 'Player2' and not state.pieceChosenForOpponent == "":   #If player 2 has placed piece, but not selected opponents piece
            return 'Player2'
        return None

    def result(self, state, move):   # use this exact signature.
        newState = deepcopy(state)
        newState.board = state.board.copy()         #Updating board
        if(state.pieceChosenForOpponent == ""):
            newState.piecesAvailable = state.piecesAvailable.copy()
        if(state.pieceChosenForOpponent == "selected"):
            state.piecesAvailable.remove(move)
            newState.piecesAvailable = state.piecesAvailable.copy()    #Updating pieces available
            newState.pieceToBePlaced = move                            #Updating piectobeplaced for oppoenent
        next_up = self.opponent(state.to_move, state)
        newState.player = next_up    #Updates the player


        # use the move to modify the newState
        return newState



    # def utility(self, state, player):   # use this exact signature.
    #     ''' return:
    #     >0 if the player is winning,
    #     <0 if the player is losing,
    #      0 if the state is a tie.
    #     '''
    #
    #     return 0

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        try:
            return state.utility if player == 'Player1' else -state.utility
        except:
            pass
        board = state.board
        util = self.check_win(board, 'Player1')
        if util == 0:
            util = -self.check_win(board, 'Player2')
        state.utility = util
        return util if player == 'Player1' else -util

    def check_win(self, board, player):
        # self.v = 7, self.h = 6
        # check columns
        for y in range(1, self.h + 1):
            for x in range(self.v - 1, 3, -1):
                if self.k_in_row(board, (x, y), (-1, 0)):
                    return 1
        # check rows
        for x in range(self.h, 0, -1):
            for y in range(1, self.v - 1):
                if self.k_in_row(board, (x, y), (0, 1)):
                    return 1

        # \ Win Check
        for y in range(self.v, 3, -1):
            for x in range(self.h, 2, -1):
                if self.k_in_row(board, (x, y), (-1, -1)):
                    return 1

        # / Win Check
        for y in range(1, self.h - 1):
            for x in range(self.v - 1, 2, -1):
                if self.k_in_row(board, (x, y), (-1, 1)):
                    return 1
        return 0


    def k_in_row(self, board, start, direction): #I have no idea if this works well
        "Return true if there is a line through start on board for player."
        (delta_x, delta_y) = direction
        x, y = start
        a, b = x + delta_x, y + delta_y #the next spot from x,y
        n = 0  # n is number of moves in row
        while board.get((x, y)) is not None:
            if self.bitwiseAND(board.get(x, y), board.get(a, b)) != 0000:
                n += 1
                x, y = x + delta_x, y + delta_y
                a, b = x + delta_x, y + delta_y   #the next spot from x,y
            elif self.bitwiseOR(board.get(x, y), board.get(a, b)) != 1111:
                n += 1
                x, y = x + delta_x, y + delta_y
                a, b = x + delta_x, y + delta_y   #the next spot from x,y

        x, y = start
        while board.get((x, y)) is not None:
            if self.bitwiseAND(board.get(x, y), board.get(a, b)) != 0000:
                n += 1
                x, y = x - delta_x, y - delta_y
                a, b = x - delta_x, y - delta_y
            elif self.bitwiseOR(board.get(x, y), board.get(a, b)) != 1111:
                n += 1
                x, y = x - delta_x, y - delta_y
                a, b = x - delta_x, y - delta_y
        n -= 1  # Because we counted start itself twice
        return n >= self.k

    def bitwiseAND(self, first, second):
        return first & second

    def bitwiseOR(self, first, second):
        return first | second

    def terminal_test(self, state):   # use this exact signature.
        # return True only when the state of the game is over.
        "A state is terminal if it is won or there are no empty squares."
        return self.utility(state, 'Player1') != 0 or len(self.actions(state)) == 0

    def display(self, state):
        board = state.board
        for x in reversed(range(1, self.h + 1)):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '....'), end='    ')
            print('\n')



myGame = TemplateGame(TemplateState)


tg = TemplateGame(TemplateState('A','','','',''))   # this is the game we play interactively.


won = TemplateState(
    player = 'Player2',
    board = {(1,1): '0010', (1,2): '1100', (1,3): '1010', (1,4): '1110',
             (2,1): '1101', (2,2): '0001',
            },
    piecesAvailable=pieces,
    pieceToBePlaced={},
    pieceChosenForOpponent=None,

    label = 'won'
)

winIn1 = TemplateState(
    player = 'Player2',
    board = {(1,2): '1100', (1,3): '1010', (1,1): '1110',
             (2,1): '1101', (2,2): '0001',
            },
    piecesAvailable=pieces,
    pieceToBePlaced=pieces[15],
    pieceChosenForOpponent=None,

    label='won'
)

myGames = {
    myGame: [
        # won,
        winIn1
    ],

    tg: [
        # TemplateState('B', {}, pieces, pieces[0],'')
        # TemplateState('C'),
    ]
}
