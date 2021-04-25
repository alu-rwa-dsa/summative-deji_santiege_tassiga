import pygame
import os

b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("img", "black_king.png"))
b_knight = pygame.image.load(os.path.join("img", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("img", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("img", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("img", "black_rook.png"))

w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))

b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (55, 55)))

for img in w:
    W.append(pygame.transform.scale(img, (55, 55)))


class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []
        self.king = False
        self.pawn = False

    def isSelected(self):
        return self.selected

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)

    def draw(self, win, color):
        if self.color == "w":
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]
            # Time Complexity is O(1)

        x = (4 - self.col) + round(self.startX + (self.col * self.rect[2] / 8))
        y = 3 + round(self.startY + (self.row * self.rect[3] / 8))

        if self.selected and self.color == color:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 62, 62), 4)

        win.blit(drawThis, (x, y))

        '''if self.selected and self.color == color:  # Remove false to draw dots
            moves = self.move_list

            for move in moves:
                x = 33 + round(self.startX + (move[0] * self.rect[2] / 8))
                y = 33 + round(self.startY + (move[1] * self.rect[3] / 8))
                pygame.draw.circle(win, (255, 0, 0), (x, y), 10)'''

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def __str__(self):
        return str(self.col) + " " + str(self.row)
    # Time Complexity is O(n)
    # The Algoorithm Varies with the square of the problem size ,n.
    # Space complexity O(1)...color takes a constant space which is not iterable
    # if block piece takes Auxiliary space


class Bishop(Piece):
    img = 0

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break

            djL += 1
            # Time Complexity is O(1)
            # The Algoorithm Varies with the square of the problem size ,n.
            # Space complexity O(n)...the parameter in this function can be iterated through


        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1
            # Time Complexity is O(n)
            # The Algoorithm Varies with the square of the problem size ,n.
            # Space complexity O(n)...the parameter in this function can be iterated through

        # TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break
            djL += 1
            # Time Complexity is O(n)
            #This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(n)...the parameter in this function can be iterated through
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1
            # Time Complexity is O(n)
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(n)...the parameter in this function can be iterated through


        return moves


class King(Piece):
    img = 1

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.king = True

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1,))
                    # Time Complexity is O(1)
                    # This means that the algorithm does a fixed number of operations no matter the number of inputs.

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

            # TOP RIGHT
            if j < 7:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))
                    # Time Complexity is O(1)
                    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                    # Space complexity O(1)...color takes a constant space which is not iterable
                    # if block piece takes Auxiliary space

        if i < 7:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))
                    # Time Complexity is O(1)
                    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                    # Space complexity O(1)...color takes a constant space which is not iterable
                    # if block piece takes Auxiliary space

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

            # BOTTOM RIGHT
            if j < 7:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))
                    # Time Complexity is O(1)
                    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                    # Space complexity O(1)...color takes a constant space which is not iterable
                    # if block piece takes Auxiliary space

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        # MIDDLE RIGHT
        if j < 7:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        return moves
    # Time Complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.


class Knight(Piece):
    img = 2

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # DOWN LEFT
        if i < 6 and j > 0:
            p = board[i + 2][j - 1]
            if p == 0:
                moves.append((j - 1, i + 2))
            elif p.color != self.color:
                moves.append((j - 1, i + 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        # UP LEFT
        if i > 1 and j > 0:
            p = board[i - 2][j - 1]
            if p == 0:
                moves.append((j - 1, i - 2))
            elif p.color != self.color:
                moves.append((j - 1, i - 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.

        # DOWN RIGHT
        if i < 6 and j < 7:
            p = board[i + 2][j + 1]
            if p == 0:
                moves.append((j + 1, i + 2))
            elif p.color != self.color:
                moves.append((j + 1, i + 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        # UP RIGHT
        if i > 1 and j < 7:
            p = board[i - 2][j + 1]
            if p == 0:
                moves.append((j + 1, i - 2))
            elif p.color != self.color:
                moves.append((j + 1, i - 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        if i > 0 and j > 1:
            p = board[i - 1][j - 2]
            if p == 0:
                moves.append((j - 2, i - 1))
            elif p.color != self.color:
                moves.append((j - 2, i - 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        if i > 0 and j < 6:
            p = board[i - 1][j + 2]
            if p == 0:
                moves.append((j + 2, i - 1))
            elif p.color != self.color:
                moves.append((j + 2, i - 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        if i < 7 and j > 1:
            p = board[i + 1][j - 2]
            if p == 0:
                moves.append((j - 2, i + 1))
            elif p.color != self.color:
                moves.append((j - 2, i + 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        if i < 7 and j < 6:
            p = board[i + 1][j + 2]
            if p == 0:
                moves.append((j + 2, i + 1))
            elif p.color != self.color:
                moves.append((j + 2, i + 1))

        return moves
    # Time Complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
    # Space complexity O(1)...color takes a constant space which is not iterable
    # if block piece takes Auxiliary space


class Pawn(Piece):
    img = 3

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.queen = False
        self.pawn = True

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        try:
            if self.color == "b":
                if i < 7:
                    p = board[i + 1][j]
                    if p == 0:
                        moves.append((j, i + 1))
                        # Time Complexity is O(1)
                        # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                        # Space complexity O(1)...color takes a constant space which is not iterable
                        # if block piece takes Auxiliary space


                    # DIAGONAL
                    if j < 7:
                        p = board[i + 1][j + 1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((j + 1, i + 1))
                                # Time Complexity is O(1)
                                # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                                # Space complexity O(1)...color takes a constant space which is not iterable
                                # if block piece takes Auxiliary space

                    if j > 0:
                        p = board[i + 1][j - 1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((j - 1, i + 1))
                                # Time Complexity is O(1)
                                # This means that the algorithm does a fixed number of operations no matter the number of inputs.

                if self.first:
                    if i < 6:
                        p = board[i + 2][j]
                        if p == 0:
                            if board[i + 1][j] == 0:
                                moves.append((j, i + 2))
                        elif p.color != self.color:
                            moves.append((j, i + 2))
                            # Time Complexity is O(1)
                            # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                            # Space complexity O(1)...color takes a constant space which is not iterable
                            # if block piece takes Auxiliary space
            # WHITE
            else:

                if i > 0:
                    p = board[i - 1][j]
                    if p == 0:
                        moves.append((j, i - 1))
                        # Time Complexity is O(1)
                        # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                        # Space complexity O(1)...color takes a constant space which is not iterable
                        # if block piece takes Auxiliary space

                if j < 7:
                    p = board[i - 1][j + 1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j + 1, i - 1))
                            # Time Complexity is O(1)
                            # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                            # Space complexity O(1)...color takes a constant space which is not iterable
                            # if block piece takes Auxiliary space

                if j > 0:
                    p = board[i - 1][j - 1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j - 1, i - 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.

                if self.first:
                    if i > 1:
                        p = board[i - 2][j]
                        if p == 0:
                            if board[i - 1][j] == 0:
                                moves.append((j, i - 2))
                        elif p.color != self.color:
                            moves.append((j, i - 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...the parameter in this function can be iterated through
        except:
            pass

        return moves


class Queen(Piece):
    img = 4

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9

            djL += 1
            # Time Complexity is O(n)
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(n)...the parameter in this function can be iterated through

        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -= 1
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9
            djL += 1
            # Time Complexity is O(n)
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(n)...the parameter in this function can be iterated through
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -= 1
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # UP
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # DOWN
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through




        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # RIGHT
        for x in range(j + 1, 8, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        return moves
    # Time Complexity is O(n)
    # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
    # Space complexity O(n)...the parameter in this function can be iterated through


class Rook(Piece):
    img = 5

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # UP
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through
        # DOWN
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through
        # RIGHT
        for x in range(j + 1, 8, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        #Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through
        # Space complexity O(n)...the parameter in this function can be iterated through
        return moves

