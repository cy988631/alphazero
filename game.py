import numpy as np

class Board:
    def __init__(self,height,width):
        self.board = np.zeros((height,width),dtype = int)
        self.current_player = 1
        self.width = width
        self.height = height
        
    def move(self,do_move):
        y = do_move % self.width
        x = do_move // self.width
        if self.board[x,y] ==0:
            self.board[x,y] = self.current_player
        else:
            return False
        self.current_player *= -1
        
    def get_availables(self):
        flatten_board = self.board.flatten()
        return np.where(flatten_board == 0)[0].tolist()