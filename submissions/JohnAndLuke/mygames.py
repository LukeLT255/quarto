from collections import namedtuple
from games import (Game)
from queue import PriorityQueue
from copy import deepcopy


class TemplateState:    # one way to define the state of a minimal game.

    def __init__(self, player, board, depth=8): # add parameters as needed.
        self.player = player
        self.board = board
        self.maxDepth = depth
        self.label = str(id(self))   # change this to something easier to read
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
    def __init__(self, initial, h, v, k):    # add parameters if needed.
        self.initial = initial
        self.h = h
        self.v = v
        self.k = k
        self.initial = TemplateState(player='Player1', board={})
        # add code and self.variables if needed.

    def actions(self, state):   # use this exact signature.
        acts = []
        # append all moves, which are legal in this state,
        # to the list of acts.
        return acts

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

    def display(self, state):   # use this exact signature.
        # pretty-print the game state, using ASCII art,
        # to help a human player understand his options.
        print(state)


myGame = TemplateGame(TemplateState, 4, 4, 4)


# tg = TemplateGame(TemplateState(''))   # this is the game we play interactively.


myGames = {
    myGame: [

    ],

    # tg: [

    # ]
}
