from Gomoku import *


if __name__ == '__main__':
    board = Gomoku()
    board.init_board()
    board.print()
    while True:
        print("O move")
        move1 = board.ask_for_move()
        board.put(move1, Color.WHITE)
        board.print()
        if board.win(Color.WHITE):
            print("O won! ")
            break
        print("X move")
        move2 = board.ask_for_move()
        board.put(move2, Color.BLACK)
        board.print()
        if board.win(Color.BLACK):
            print("X won! ")
            break

