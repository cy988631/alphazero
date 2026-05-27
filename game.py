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
        print('  ',end = ' ')
        char_map = {1:'o',-1:'●',0:'.'}
        for col in range(self.width):
            print(f'{col:2d}',end = ' ')
        print()
        for row in range(self.height):
            print(f'{row:2d}',end = ' ')
            for col in range(self.width):
                print(f'{char_map[self.board[row,col]]:>2}',end = ' ')
            print()
            
    def copy(self):
        copy_board = Board(self.height , self.width)
        copy_board = self.board.copy()
        copy_board.current_player = self.current_player
        return copy_board

if __name__ == '__main__':

    test_board = Board(9,9)

    while(True):
        test_board.render()
        test_player = " 黑方 " if test_board.current_player == 1 else " 白方 "
        test_move = input(f'当前玩家为{test_player}:')
        row_str , col_str = test_move.split(',')
        row = int(row_str)
        col = int(col_str)
        move_int = row * test_board.width + col
        test_board.move(move_int)
        is_end , winner = test_board.check_win(move_int)
        if is_end == True:
            test_board.render()
            if winner == 1:
                print(f'{test_player}胜利！')
                break
            if winner == -1:
                print(f'{test_player}胜利！')
                break
            elif winner == 0:
                print(f'平局！')
                break
            else:
                continue
              