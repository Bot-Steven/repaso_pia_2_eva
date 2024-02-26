import random
import configparser
from game import Game 

class DungeonCrawl(Game):

    def game_init(self, config):
        config_parser = configparser.ConfigParser()
        config_parser.read(config)

        # Asignar valores desde el archivo de configuración
        self.width = config_parser.getint("DungeonCrawl", "mapa_ancho")
        self.height = config_parser.getint("DungeonCrawl", "mapa_alto")
        self.pct = config_parser.getfloat("DungeonCrawl", "pct_paredes")

        # creamos el mapa 
        self.create_grid()
        # Inicializar posición del jugador
        self.player_x, self.player_y = 0, 0  
        # Meta
        self.end_x, self.end_y = self.width - 1, self.height - 1  

    def game_input(self) -> str:
        return input("Camino a seguir (l/r/u/d): ") 

    def game_turn(self, input_str):
        if input_str.lower() in ["l", "r", "u", "d"]:
            self.move_player(input_str.lower())
        else:
            print("Entrada inválida. Por favor, usa 'l', 'r', 'u', 'd' para moverte.")

    def game_print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.map[y][x], end=" ")
            print()

    def game_is_finish(self) -> bool:
        return (self.player_x, self.player_y) == (self.end_x, self.end_y)

    def game_finish_msg(self) -> str:
        return print("¡Felicidades! Has llegado a la salida.")

    def create_grid(self):
        path_found = False
        while not path_found:
            self.map = [[] for y in range(self.height)]
            for y in range(self.height):
                for x in range(self.width):
                    self.map[y].append(". ")

            # posicion inicial del jugador
            self.player_x = 0
            self.player_y = 0
            # posición inicial del jugador
            self.map[self.player_y][self.player_x] = "$ "
            # entrada en la esquina superior izquierda
            self.start_x, self.start_y = 0, 0
            # salida en la esquina inferior derecha
            self.end_x, self.end_y = self.width - 1, self.height - 1
            # representa la salida
            self.map[self.end_y][self.end_x] = "> "

            # Generar y colocar paredes
            self.get_walls()

            # Comprobar si hay un camino disponible
            self.visited = set()
            path_found = self.path_exist(self.start_y, self.start_x)


    def get_walls(self):
        num_walls = round((self.width * self.height * self.pct)/2)
        # tupla de dos valores
        coordinates = list()
        # obtener todas las coordenadas posibles 
        for y in range(self.height):
            for x in range(self.width):
                coordinates.append((x, y))
        # eliminar de coordinates entrada y salida
        coordinates.remove((self.start_x, self.start_y))
        coordinates.remove((self.end_x, self.end_y))
        # shuffle mezcla aleatoriamente la tupla
        random.shuffle(coordinates)
        # coger las primeras num_walls(67) elementos
        chosen = coordinates[:num_walls]

        for x, y in chosen:
            self.map[y][x] = "# "

    def move_player(self, direction):
        new_x, new_y = self.player_x, self.player_y
        if direction == "r" and self.player_x < self.width - 1:
            new_x += 1
        elif direction == "l" and self.player_x > 0:
            new_x -= 1
        elif direction == "u" and self.player_y > 0:
            new_y -= 1
        elif direction == "d" and self.player_y < self.height - 1:
            new_y += 1

        # verificar si la nueva posición está dentro de la lista de muros
        if self.map[new_y][new_x] != "# ":
            # limpiar la posición actual del jugador
            self.map[self.player_y][self.player_x] = ". "
            # actualizar la posición del jugador en el mapa
            self.player_x, self.player_y = new_x, new_y
            # volver a actulizar el simbolo del jugador
            self.map[self.player_y][self.player_x] = "$ "
        else:
            # la nueva posición es un muro, el jugador no se mueve
            print("There is a wall!")

    def path_exist(self, y, x):
        if (y, x) == (self.end_y, self.end_x):
            # Se ha encontrado la salida
            return True

        if (y, x) not in self.visited and self.map[y][x] != "# ":
            self.visited.add((y, x))

            for direction in ["r", "d", "l", "u"]:
                new_y, new_x = y, x
                if direction == "r" and new_x < self.width - 1:
                    new_x += 1
                elif direction == "l" and new_x > 0:
                    new_x -= 1
                elif direction == "u" and new_y > 0:
                    new_y -= 1
                elif direction == "d" and new_y < self.height - 1:
                    new_y += 1

                if (new_y, new_x) not in self.visited:
                    if self.path_exist(new_y, new_x):
                        # Se encontró un camino en la nueva coordenada
                        return True
        return False
    