from collections import namedtuple
from games import (Game)
from queue import PriorityQueue
from copy import deepcopy
import numpy as np


pieces = [0b0000, 0b0001, 0b0010, 0b0011, 0b0100, 0b0101, 0b0110, 0b0111, 0b1000, 0b1001, 0b1010,
          0b1011, 0b1100, 0b1101, 0b1110, 0b1111, ]




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
        # use the move to modify the newState
        return newState

    def terminal_test(self, state):   # use this exact signature.
        # return True only when the state of the game is over.
        return True

    def utility(self, state, player):   # use this exact signature.
        ''' return:
        >0 if the player is winning,
        <0 if the player is losing,
         0 if the state is a tie.
        '''

        return 0


    def display(self, state):
        board = state.board
        for x in reversed(range(1, self.h + 1)):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '....'), end='    ')
            print('\n')



myGame = TemplateGame(TemplateState, 4, 4, 4)


tg = TemplateGame(TemplateState('A','','','',''))   # this is the game we play interactively.


won = TemplateState(
    player = 'Player2',
    board = {(1,1): '0010', (1,2): '1100', (1,3): '1010', (1,4): '1110',
             (2,1): '1101', (2,2): '0001',
            },
    piecesAvailable={},
    pieceToBePlaced={},
    pieceChosenForOpponent=None,

    label = 'won'
)

myGames = {
    myGame: [
        # won,
    ],

    tg: [
        TemplateState('B','','','','')
        # TemplateState('C'),
    ]
}
