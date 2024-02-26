import random as rm
import configparser
from game import Game 

class GameOfLife(Game):
    ALIVE = "🟩"
    DEAD = "🟥"

    def game_init(self, config):
        config_parser = configparser.ConfigParser()
        config_parser.read(config)

        # Asignar valores desde el archivo de configuración
        self.width = config_parser.getint("GameOfLife", "ancho")
        self.height = config_parser.getint("GameOfLife", "alto")
        self.init_alive_cells_num = config_parser.getint("GameOfLife", "num_celulas_vivas_iniciales")
        self.game_turns = config_parser.getint("GameOfLife", "num_turnos")
        self.cells = []
        self.mapa = [[False] * self.width for _ in range(self.height)]
        self.set_init_alive_cells()
        self.draw_grid()

    def game_input(self) -> str:
        pass

    def game_turn(self, input_str):
        self.next_turn_grid()

    def game_print(self):
        self.draw_final_grid()

    def game_is_finish(self) -> bool:
        self.game_turns -= 1
        return self.game_turns <= 0

    def game_finish_msg(self) -> str:
        return print("El juego de la vida ha terminado.")
    
    def draw_grid(self): 
        k = 0
        for i in range(self.height):
            for j in range(self.width):
                if (k < len(self.cells)) and (self.cells[k][0] == i and self.cells[k][1] == j):
                    print(self.ALIVE, end=" ")
                    self.mapa[i][j] = True
                    k += 1 
                else:
                    print(self.DEAD, end=" ")
                    self.mapa[i][j] = False
            print("\n ")

    def set_init_alive_cells(self):
        my_set = set()

        while len(my_set) < self.init_alive_cells_num:
            fil=rm.randint(0, self.height - 1)
            col=rm.randint(0, self.width - 1)
            my_set.add((fil,col)) 
        
        self.cells = list(my_set)
        self.cells.sort()

    def next_turn_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                vivas = self.get_cell_living_neighbors(y, x) 
                
                if self.mapa[y][x] == True:
                    if vivas < 2:
                        self.mapa[y][x] = False
                    elif 2 <= vivas <= 3:    
                        self.mapa[y][x] = True   
                    elif vivas > 3:
                        self.mapa[y][x] = False
                else:
                    if vivas == 3:
                        self.mapa[y][x] = True

    def draw_final_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.mapa[i][j] == True:
                    print(self.ALIVE, end=" ") 
                else:
                    print(self.DEAD, end=" ")
            print("\n ")

    def get_cell_living_neighbors(self, y, x):
        count = 0
        posicionesRelativas = [
            (-1, 0),  #  hacia arriba
            (1, 0),   #  hacia abajo
            (0, -1),  #  hacia la izquierda
            (0, 1),   #  hacia la derecha
            (-1, -1), #  diagonal superior izquierda
            (-1, 1),  #  diagonal superior derecha
            (1, -1),  #  diagonal inferior izquierda
            (1, 1)    #  diagonal inferior derecha
        ]
        
        for i, j in posicionesRelativas:
            new_y = y + j
            new_x = x + i

            if (0 > new_x) or (0 > new_y) or (self.height <= new_y) or (self.width <= new_x):
                continue
            else:
                if self.mapa[new_y][new_x] == True:
                    count += 1

        return count