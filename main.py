from game import Board
from aiplayers.mcts_ai import MCTSAI
from aiplayers.normal_ai import Human,RuleAI

state = Board(9,9)

#人类vs普通随机ai
players = {1:MCTSAI(),-1:Human()}

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
            print('MCTSAI胜利！')
            break
        if winner == -1:
            print('Human胜利！')
            break
        elif winner == 0:
            print(f'平局！')
            break
        else:
            continue