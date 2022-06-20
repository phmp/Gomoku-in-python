from enum import Enum


class Color (Enum):
    EMPTY = 1
    BLACK = 2
    WHITE = 3

    def sign(self):
        if self == Color.EMPTY:
            return ' ' + chr(176) + ' '
        elif self == Color.BLACK:
            return ' X '
        else:
            return ' O '


class Gomoku:
    board = [[]]
    ySize = 8
    xSize = 8

    def init_board(self):
        board = []
        for i in range(self.xSize):
            row = []
            for j in range(self.ySize):
                row.append(Color.EMPTY)
            board.append(row)
        self.board = board

    def print(self):
        print("")
        for row in self.board:
            line = ''
            for element in row:
                line = line + element.sign()
            print(line)

    def put(self, point, color):
        x = point[0]
        y = point[1]
        if self.board[x][y] == Color.EMPTY:
            self.board[x][y] = color
        else:
            print('ERROR!!')

    def win(self, color):
        for x in range(self.xSize-4):
            for y in range(self.ySize):
                if (self.board[x][y] == color)\
                        and (self.board[x+1][y] == color) \
                        and (self.board[x+2][y] == color) \
                        and (self.board[x+3][y] == color) \
                        and (self.board[x+4][y] == color):
                    return True
        for x in range(self.xSize):
            for y in range(self.ySize-4):
                if (self.board[x][y] == color)\
                        and (self.board[x][y+1] == color) \
                        and (self.board[x][y+2] == color) \
                        and (self.board[x][y+3] == color) \
                        and (self.board[x][y+4] == color):
                    return True
        for x in range(self.xSize-4):
            for y in range(self.ySize-4):
                if (self.board[x][y] == color)\
                        and (self.board[x+1][y+1] == color) \
                        and (self.board[x+2][y+2] == color) \
                        and (self.board[x+3][y+3] == color) \
                        and (self.board[x+4][y+4] == color):
                    return True
        for x in range(4, self.xSize):
            for y in range(self.ySize-4):
                if (self.board[x][y] == color)\
                        and (self.board[x-1][y+1] == color) \
                        and (self.board[x-2][y+2] == color) \
                        and (self.board[x-3][y+3] == color) \
                        and (self.board[x-4][y+4] == color):
                    return True
        return False


game = Gomoku()
game.init_board()
game.put((0, 0), Color.WHITE)
game.put((1, 1), Color.BLACK)
game.print()
print('BLACK won ' + str(game.win(Color.BLACK)))
print('WHITE won ' + str(game.win(Color.WHITE)))
