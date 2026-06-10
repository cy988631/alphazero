from game import Board
import math
import random

class MCTSnode():
    #创建节点
    def __init__(self,parent,action,board):
        self.parent = parent
        self.children = {}
        self.wins = 0
        self.visits = 0
        self.action = action
        self.board = board.copy()
    
    def get_UCB(self):
        #UCB判分
        if self.visits == 0:
            return float('inf')
        else:
            exploitation = self.wins/self.visits
            exploration = math.sqrt(2)*math.sqrt(math.log(self.parent.visits)/self.visits)
            return exploitation + exploration
            
    def get_max(self):
        #找最高得分
        if self.children == {}:
            return False
        else:
            return max(self.children.values(),key = MCTSnode.get_UCB())
        
class MCTS():
    #主流程
    def __init__(self,board):
        #初始化棋盘和当前节点
        self.board = board
        self.node = MCTSnode(None,None,self.board)
    
    def selection(self):
        #选择
        while(len(self.node.board.get_availables()) == len(self.node.children)):
            self.node = self.node.get_max()
            if len(self.node.children == 0):
                break
            
    def expansion(self):
        #扩展
        move = random.choice(self.node.board.get_availables())
        new_board = self.node.board.copy()
        new_board.move()
        new_node = MCTSnode(self.node,move,new_board)
        self.node.children.update(move:new_node)
        self.node = self.node.get_max()

    