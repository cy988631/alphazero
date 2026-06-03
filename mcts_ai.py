from game import Board
import math

class MCTSnode():
    def __init__(self,parent,action):
        self.parent = parent
        self.children = {}
        self.wins = 0
        self.visits = 0
        self.action = action
        
    def get_UCB(self,c_param):
        if self.visits == 0:
            return float('inf')
        else:
            exploitation = self.wins/self.visits
            self.c_param = c_param
            exploration = self.c_param*math.sqrt(math.log(self.parent.visits)/self.visits)
            return exploitation + exploration

class MCTS():
    def selection(self,board):
