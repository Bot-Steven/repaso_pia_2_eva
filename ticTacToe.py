from os import system
from game import Game
from random import randint
import numpy as np

def numeric_2_position(numeric):
        if numeric == 7:
            return 0, 0
        elif numeric == 8:
            return 0, 1
        elif numeric == 9:
            return 0, 2
        elif numeric == 4:
            return 1, 0
        elif numeric == 5:
            return 1, 1
        elif numeric == 6:
            return 1, 2
        elif numeric == 1:
            return 2, 0
        elif numeric == 2:
            return 2, 1
        elif numeric == 3:
            return 2, 2
        else:
            return -1, -1

# eq significa equivalente (si son iguales o no)
# i en este def es columnas 
def check_arr(board):
    eq = False
    val = board[0]
    for i in range(len(board)):
        if val != board[i]:
            break
    else:
        if val != 0:
            eq = True
    return eq

def check_rows(board):
    eq = False
    for i in range(len(board)):
        eq = check_arr(board[i])
        if eq:
            break
    return eq


def check_cols(board):
    eq = False
    for i in range(len(board[0])):
        eq = check_arr([row[i] for row in board])
        if eq:
            break
    return eq


def check_diags(board):
    eq = False
    l = len(board)
    if check_arr([board[i][i] for i in range(l)]):
        eq = True
    elif check_arr([board[l - 1 - i][i] for i in range(l - 1, -1, -1)]):
        eq = True
    return eq

# si el jugador actual ha ganado
# mirando la fila, columna y diagonal
def has_won(board):
    won = False
    if check_rows(board):
        won = True
    elif check_cols(board):
        won = True
    elif check_diags(board):
        won = True
    return won

# recorriendo el tablero i (filas) y j (columnas)
def is_full(board):
    full = True
    for i in range(0, len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                full = False

    return full


class TicTacToe(Game):

    def __init__(self):
        self.players = []
        self.first_player_idx = 0
        self.second_player_idx = 0
        self.board = []
        self.current_player = 0

    def game_init(self, config): 
        # players = [' ', 'O', 'X'] 
        self.players = config['players']

        # randomizar jugador
        self.first_player_idx = 1 if randint(0, 1) == 0 else -1
        self.second_player_idx = 1 if self.first_player_idx == -1 else -1
        
        # rellenar tablero 3x3 a 0
        self.board = [
            ["0" for row in range(3)] 
                for col in range(3)
            ]
        
        # asignar jugador actual
        self.current_player = self.first_player_idx

    def game_input(self) -> str:
        return input("Introduce tu movimiento (1-9): " + self.players[self.current_player] + "\n>")

    def game_turn(self, input_str):
        # traducir el valor del teclado numerico al tabler (indices)
        row, col = numeric_2_position(int(input_str))

        # si se introduce un valor que no esta entre 1-9
        if (row == -1) & (col == -1):
            return
        
        # si el tablero no esta vacío en esa posicion
        if self.board[row][col] != 0:
            return

        # valor introducido por el jugador actual 
        self.board[row][col] = self.current_player

        # cambiar de jugador
        self.current_player *= -1

    def game_print(self):
        _ = system('clear')
        print("############################################################")
        print("###################### TIC TAC TOE  ########################")
        print("############################################################")
        print("")
        print("+---+---+---+")
        print(" | " + str(self.players[self.board[0][0]]) +
              " | " + str(self.players[self.board[0][1]]) +
              " | " + str(self.players[self.board[0][2]]) + " |")
        print("+---+---+---+")
        print(" | " + str(self.players[self.board[1][0]]) +
              " | " + str(self.players[self.board[1][1]]) +
              " | " + str(self.players[self.board[1][2]]) + " |")
        print("+---+---+---+")
        print(" | " + str(self.players[self.board[2][0]]) +
              " | " + str(self.players[self.board[2][1]]) +
              " | " + str(self.players[self.board[2][2]]) + " |")
        print("+---+---+---+")

    def game_is_finish(self) -> bool:
        finish = False
        
        if has_won(self.board):
            finish = True
        elif is_full(self.board):
            finish = True

        return finish

    def game_finish_msg(self) -> str:
        pass