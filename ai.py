from game import Board
import random

state = Board(15,15)

class RandomAI():
    def get_action(self,board):
        do_move = random.choice(board.get_availables())
        return do_move
    
class RuleAI():
    def get_action(self,board):
        # 拿到空位
        availables = board.get_availables()
        
        my_color = board.current_player
        opponent_color = -my_color
        
        for move in availables:
            # 寻找我方绝杀点
            row , col = move // board.width , move % board.width
            board.board[row,col] = my_color
            is_end , winner = board.check_win(move)
            board.board[row,col] = 0
            if is_end and winner == my_color:
                return move
        
        for move in availables:
            # 寻找敌方绝杀点
            row , col = move // board.width , move % board.width
            board.board[row,col] = opponent_color
            is_end , winner = board.check_win(move)
            board.board[row,col] = 0
            if is_end and winner == opponent_color:
                return move
            
        return random.choice(board.get_availables())
    
class Human:
    def get_action(self,board):
        while(True):
            try:
                # 人类落子逻辑
                do_move = input(f'请输入坐标：')
                row_str , col_str = do_move.split(',')
                row = int(row_str)
                col = int(col_str)
                
                #  边界检查：防止你输入 99,99 导致底层矩阵索引越界崩溃
                if row < 0 or row >= board.width or col < 0 or col >= board.height:
                    print("⚠️ 坐标越界了，请重新输入！")
                    continue
                            
                # 降维打击：将二维转为一维 
                move = row * board.width + col
                        
                # 合法性检查：看看这地方是不是已经有棋子了
                availables = board.get_availables()
                if move not in availables:
                    print("⚠️ 这个位置已经有子了，请换个空位！")
                    continue
                
                return move
            except ValueError:
                print("❌ 输入格式错误！请重新输入！")

players = {1:RuleAI(),-1:Human()}

while(True):
    state.render()
    ai_player = players[state.current_player]
    print(f'当前玩家:{ai_player}思考中')
    move = ai_player.get_action(state)
    state.move(move)
    is_end , winner = state.check_win(move)
    if is_end == True:
        state.render()
        if winner == 1:
            print('RuleAI胜利！')
            break
        if winner == -1:
            print('Human胜利！')
            break
        elif winner == 0:
            print(f'平局！')
            break
        else:
            continue