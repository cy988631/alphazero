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
    
    def check_win(self,do_move):
        y = do_move % self.width
        x = do_move // self.width
        color = self.board[x,y]
        
        for dx,dy in [(0,1),(1,1),(1,0),(1,-1)]:
            count = 1
            nx = x+dx
            ny = y+dy
            while(True):
                if 0 <= nx <= self.height-1 and 0 <= ny <= self.width-1:
                    if self.board[nx,ny] == color:
                        count += 1
                        nx += dx
                        ny += dy
                    else:
                        break
                else:
                    break
            
            nx = x-dx
            ny = y-dy
            while(True):
                if 0 <= nx <= self.height-1 and 0 <= ny <= self.width-1:
                    if self.board[nx,ny] == color:
                        count += 1
                        nx -= dx
                        ny -= dy
                    else:
                        break
                else:
                    break
                
            if count>=5:
                 return True,color
                
        if len(self.get_availables()) == 0:
            return True,0
        
        return False,-1
    
    def render(self):
        print(' ',end = ' ')
        char_map = {1:'o',-1:'●',0:'.'}
        for col in range(self.width):
            print(col,end = ' ')
        print()
        for row in range(self.height):
            print(row,end = ' ')
            for col in range(self.width):
                print(char_map[self.board[row,col]],end = ' ')
            print()


test = Board(15,15)