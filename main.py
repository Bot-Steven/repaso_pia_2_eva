import os
import time
from ticTacToe import TicTacToe
from dungeonCrawl import DungeonCrawl
from gameOfLife import GameOfLife

def clear():
    # Para Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Para Unix/Linux
    else:
        _ = os.system('clear')

finish = False
config = "config.ini"

while not finish:
    # Seleccionar el juego 
    print("Seleccione un juego:\n"
      "1 - TicTacToe\n"
      "2 - Dungeon Crawl\n"
      "3 - Game of Life\n"
      "4 - Salir")
    
    game_choice = input("Tu selección: ")
    is_game_of_life = False

    if game_choice == '1':
        gm = TicTacToe()
    elif game_choice == '2':
        gm = DungeonCrawl()
    elif game_choice == '3':
        gm = GameOfLife()
        is_game_of_life = True
    elif game_choice == '4':
        print("Bye!")
        break
    else:
        print("Selección no válida. Por favor, elige un número entre 1 y 4.")
        continue

    gm.game_init(config)
    gm.game_print()

    while not gm.game_is_finish():
        gm.game_turn(gm.game_input())
        # Solo dormir si es Game of Life
        if is_game_of_life:
            time.sleep(1)  
        # Limpia la pantalla
        clear()
        gm.game_print()

    gm.game_finish_msg()
    time.sleep(1)

    # Pregunta al usuario si quiere jugar de nuevo o terminar
    play_again = input("¿Jugar de nuevo? (y/n): ")
    if play_again.lower() != 'y':
        finish = True