def create_board():
    """
    新建一个3*3的棋盘
    这里的字符串最好给一个空格，否则打印出来的效果会棋盘偏移
    """
    return [[' ', ' ', ' '] for _ in range(3)]

def print_board(board):
    """
    打印棋盘
    """
    print("        1   2   3  ")
    print("      +---+---+---+")
    for i, row in enumerate(board, start = 1):
        print(f"    {i} | " + ' | '.join(row) + ' | ')
        if i <= 3:
            print("      +---+---+---+")
    print()

def play_one_round():
    """
    先手用'X'，后手用'O'
    """
    board = create_board()
    current_player = 'X'
    while True:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player

        game_over, winner = check_winner(board)
        if game_over:
              print_board(board)  # ✅ 游戏结束后再打印一次最终棋盘，让用户看到结果
              if winner is not None:
                  print(f"玩家 {winner} 获胜！🎉")
              else:
                  print("平局！🤝")
              break

        # 交换玩家继续
        current_player = 'O' if current_player == 'X' else 'X'

def get_move(board, player):
    while True:
        try:
            x, y = input(f"Player {player}, enter your move (row col):").split()
            row = int(x)
            col = int(y)
        except ValueError:
              print("❌ 输入格式错误，请输入两个数字，用空格分隔！")
              continue

        if row < 1 or row > 3 or col < 1 or col > 3:
            print("❌ 坐标范围错误！行和列都必须在 1~3 之间。")
            continue

        if board[row-1][col-1] != ' ':
            print(f"❌ 该位置已有棋子 [{board[row-1][col-1]}]，请换位置！")
            continue

        return row-1, col-1

def check_winner(board):
    win_lines = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)]
    ]

    for win_line in win_lines:
        a, b, c = win_line
        arow, acol = a
        brow, bcol = b
        crow, ccol = c
        if board[arow][acol] == board[brow][bcol] == board[crow][ccol] != ' ':
            return (True, board[arow][acol])

    is_full = all(cell != ' ' for row in board for cell in row)
    if is_full:
        return (True, None)
    
    return (False, None)

if __name__ == "__main__" :
      print("🎉  欢迎来到 Jabin 的井字棋游戏！🎉")
      while True:
          start_flag = input("\n是否开始新游戏？(Y 开始 / N 退出): ")
          if start_flag.strip().upper() == 'Y':
              play_one_round()
          elif start_flag.strip().upper() == 'N':
              print("👋  再见！欢迎下次再来玩！")
              break
          else:
              print("❌  输入错误，请输入 Y 或者 N！")