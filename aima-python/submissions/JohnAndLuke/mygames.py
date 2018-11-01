from collections import namedtuple
from games import (Game)
from queue import PriorityQueue
from copy import deepcopy


class TemplateState:    # one way to define the state of a minimal game.

    def __init__(self, player): # add parameters as needed.


    def __str__(self):  # use this exact signature



class TemplateGame(Game):

    def __init__(self, initial):    # add parameters if needed.



    def actions(self, state):   # use this exact signature.


    def result(self, state, move):   # use this exact signature.


    def terminal_test(self, state):   # use this exact signature.


    def utility(self, state, player):   # use this exact signature.


    def display(self, state):   # use this exact signature.




myGames = {
    myGame: [

    ],

    tg: [
        # these are the states we tabulate when we test AB(1), AB(2), etc.

    ]
}
