from enum import Enum


class Color(Enum):
    EMPTY = 1
    BLACK = 2
    WHITE = 3

    def sign(self):
        if self == Color.EMPTY:
            return ' - '
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
        for x in range(self.xSize - 4):
            for y in range(self.ySize):
                if (self.board[x][y] == color) \
                        and (self.board[x + 1][y] == color) \
                        and (self.board[x + 2][y] == color) \
                        and (self.board[x + 3][y] == color) \
                        and (self.board[x + 4][y] == color):
                    return True
        for x in range(self.xSize):
            for y in range(self.ySize - 4):
                if (self.board[x][y] == color) \
                        and (self.board[x][y + 1] == color) \
                        and (self.board[x][y + 2] == color) \
                        and (self.board[x][y + 3] == color) \
                        and (self.board[x][y + 4] == color):
                    return True
        for x in range(self.xSize - 4):
            for y in range(self.ySize - 4):
                if (self.board[x][y] == color) \
                        and (self.board[x + 1][y + 1] == color) \
                        and (self.board[x + 2][y + 2] == color) \
                        and (self.board[x + 3][y + 3] == color) \
                        and (self.board[x + 4][y + 4] == color):
                    return True
        for x in range(4, self.xSize):
            for y in range(self.ySize - 4):
                if (self.board[x][y] == color) \
                        and (self.board[x - 1][y + 1] == color) \
                        and (self.board[x - 2][y + 2] == color) \
                        and (self.board[x - 3][y + 3] == color) \
                        and (self.board[x - 4][y + 4] == color):
                    return True
        return False

    def is_in_side(self, point):
        x = point[0]
        y = point[1]
        return (x >= 0) and (x < self.xSize) and (y >= 0) and (y < self.ySize)

    def is_empty(self, point):
        x = point[0]
        y = point[1]
        return self.board[x][y] == Color.EMPTY

    def ask_for_move(self):
        repeat = True
        x = ''
        y = ''
        while repeat:
            print("Please provide index of row: ")
            x = input()

            print("Please provide index of column: ")
            y = input()

            repeat = not self.is_valid(x, y)

        print("Move is " + x + ' ' + y)
        return int(x), int(y)

    def is_valid(self, x, y):
        if not x.isnumeric():
            print("x is not numeric")
            return False
        if not y.isnumeric():
            print("y is not numeric")
            return False
        move = (int(x), int(y))

        if not self.is_in_side(move):
            print("Field is out side of the board")
            return False

        if not self.is_empty(move):
            print("Field is already taken")
            return False

        return True
