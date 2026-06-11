from game import Board
import math
import numpy as np
import random

class MCTSnode():
    #创建节点
    def __init__(self,parent,action,board):
        self.parent = parent
        self.children = {}
        self.wins = 0
        self.visits = 0
        self.action = action
        self.board = board
        
        #终局判定
        self.is_terminal = False
        if action is not None and self.board.check_win(action) != (False,-1) :
            self.is_terminal = True
        
    
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
            #判断是否还有子节点和是否结束
            if self.node.is_terminal or len(self.node.children) == 0:
                break

            self.node = self.node.get_max()
            
    def expansion(self):
        #扩展
        
        #终局判定
        if self.node.is_terminal:
            return
        
        #获取空位并过滤未探索动作
        availables = np.array(self.node.board.get_availables())
        explored_moves = list(self.node.children.keys())
        unexplored_moves = availables[~np.isin(availables,explored_moves)] 
        do_move = np.random.choice(unexplored_moves)
        
        #扩展并更新节点
        new_board = self.node.board.copy()
        new_board.move(do_move)
        new_node = MCTSnode(self.node,do_move,new_board)
        self.node.children[do_move] = new_node
        self.node = new_node

    def simulation(self):
        #模拟
        sim_board = self.node.board.copy()
        while True:
            #平局判断
            if len(sim_board.get_availables()) == 0:
                return -1
            #落子
            do_move =random.choice(sim_board.get_availables())
            sim_board.move(do_move)
            #赢家检测
            win_flag , win_player = sim_board.check_win(do_move)
            if win_flag:
                return win_player
            
    def backpropagation(self):
        #回传
        