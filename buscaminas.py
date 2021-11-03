import random

def create_board(rows, cols, bombs):
    board = [[' ' for x in range(rows)] for y in range(cols)]
    i = 0
    while i < bombs:
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-1)
        if board[row][col] == ' ':
            board[row][col] = 'B'
            i += 1
    for a in range(rows):
        for b in range(cols):
            if board[a][b] == ' ':
                raux = a-1
                aux = 0
                for raux2 in range(3):
                    caux = b-1
                    for caux2 in range(3):
                        if raux+raux2 >= 0 and raux+raux2 < rows and caux+caux2>=0 and caux+caux2<cols :
                            if board[raux+raux2][caux+caux2] == "B":
                                aux += 1
                if aux == 0:
                    board[a][b] = ' '
                else:
                    board[a][b] = str(aux)
    return board




class Buscaminas:
    def __init__(self, rows = 0, cols = 0, bombs = 0):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = create_board(self.rows, self.cols, self.bombs)
        self.show = [['-' for x in range(rows)] for y in range(cols)]

    def show_board(self):
        print("Tabla Jugar")
        for row in self.show:
            print(row)  
        print("Tabla Trampa")
        for row in self.board:
            print(row)

    def win(self):
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.show[i][j] == 'F' and self.board[i][j] == 'B':
                    count +=1
        return count == self.bombs

    def lose(self):
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.show[i][j] == 'B':
                    count +=1
        return count != 0

    def question(self, movs):
        mov = input("Elija si descubrir o marcar una bandera: ")
        row = int(input("Elija el numero de fila: "))
        col = int(input("Elija el numero de columna: "))
        if mov not in movs or row > self.rows or col > self.cols:
            raise Exception
        else:
            row = int(row)
            col = int(col)
            mov = str(mov)
        return mov, row, col

    def play(self, mov, row, col):
        if mov == 'uncover':
            self.show[row][col] = self.board[row][col]
        if mov == 'flag':
            self.show[row][col] = 'F'