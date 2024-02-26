import random
import configparser
from game import Game 

class TicTacToe(Game):

    def game_init(self, config):
        config_parser = configparser.ConfigParser()
        config_parser.read(config)

        # Asignar valores desde el archivo de configuración
        self.tamano_tablero = config_parser.getint("TicTacToe", "tablero_tamano")
        self.jugador1_simbolo = config_parser.get("TicTacToe", "jugador1_simbolo")
        self.jugador2_simbolo = config_parser.get("TicTacToe", "jugador2_simbolo")
        self.jugador_inicial_config = config_parser.get("TicTacToe", "jugador_inicial")
    
        # Inicializar el tablero
        self.tablero = [[" " for y in range(self.tamano_tablero)] for x in range(self.tamano_tablero)]
        self.tablero_num = [[7, 8, 9],[4, 5, 6],[1, 2, 3]]

        # Determinar el jugador inicial
        if self.jugador_inicial_config == "aleatorio":
            self.jugador_actual = random.randint(0, 1)
        elif self.jugador_inicial_config == "jugador1":
            self.jugador_actual = 0
        else:
            self.jugador_actual = 1

    def game_input(self) -> str:
        return input("Introduce tu movimiento (1-9): ")
    
    def game_turn(self, input_str):
        movimiento = int(input_str)

        for x in range(len(self.tablero_num)):
            for y in range(len(self.tablero_num[x])):
                if self.tablero_num[x][y] == movimiento:
                    if self.tablero[x][y] == " ":
                        # Asignar el símbolo del jugador actual al tablero
                        if self.jugador_actual == 0:
                            self.tablero[x][y] = self.jugador1_simbolo
                        else:
                            self.tablero[x][y] = self.jugador2_simbolo
                        
                        # Cambiar al otro jugador
                        if self.jugador_actual == 0:
                            self.jugador_actual = 1
                        else:
                            self.jugador_actual = 0

                        return True
                    else:
                        print("¡Casilla ocupada! Elige otra posición.")
                        return False
         # Si el movimiento no se encuentra en tablero_num            
        return False 

    def game_print(self):
        print("+----+----+----+")
        print("| " + self.tablero[0][0] + "  | " + self.tablero[0][1] + "  | " + self.tablero[0][2] + "  |")
        print("+----+----+----+")
        print("| " + self.tablero[1][0] + "  | " + self.tablero[1][1] + "  | " + self.tablero[1][2] + "  |")
        print("+----+----+----+")
        print("| " + self.tablero[2][0] + "  | " + self.tablero[2][1] + "  | " + self.tablero[2][2] + "  |")
        print("+----+----+----+")

    def game_is_finish(self) -> bool:
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] and self.tablero[i][0] != " ":
                return True
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] and self.tablero[0][i] != " ":
                return True
            if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] and self.tablero[0][0] != " ":
                return True
            if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] and self.tablero[0][2] != " ":
                return True
        return False

    def game_finish_msg(self) -> str:
        if self.game_is_finish():
            ganador = self.jugador2_simbolo if self.jugador_actual == 0 else self.jugador1_simbolo
            return print("¡Felicidades! El jugador con", ganador, "ha ganado.")
        else:
            return print("Es un empate.")