from game import Board
import math

class MCTSnode():
    #创建节点
    def __init__(self,parent,action):
        self.parent = parent
        self.children = {}
        self.wins = 0
        self.visits = 0
        self.action = action
    
    def get_UCB(self,c_param=math.sqrt(2)):
        #UCB判分
        if self.visits == 0:
            return float('inf')
        else:
            exploitation = self.wins/self.visits
            self.c_param = c_param
            exploration = self.c_param*math.sqrt(math.log(self.parent.visits)/self.visits)
            return exploitation + exploration
            
    def get_max(self):
        #找最高得分
        if self.children == {}:
            return False
        else:
            return max(self.children,key = self.get_UCB())
class MCTS():
    #主流程
    def __init___(self,board):
        self.board = board
        self.node = MCTSnode()
    def selection(self):
        copy_board = self.board.copy()



