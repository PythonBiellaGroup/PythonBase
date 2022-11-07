import random
import os
import sys


def print_grid(rows, cols, grid):

    output = ""
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                output += ". "
            else:
                output += "@ "
        output += "\n\r"
    print(output, end=" ")


def print_initial_grid(rows: int, cols: int) -> list:
    """
    Stampa la griglia iniziale all'inizio del gioco
    Args:
        rows (int): Righe della griglia iniziale
        cols (int): Colonne della griglia iniziale

    Returns:
        list: La griglia iniziale con le cellule generate.
    """

    # Stampa la griglia iniziale
    grid = []
    for _ in range(rows):  # questo è un ciclo sulle righe
        grid_rows = []
        for _ in range(cols):
            if random.randint(0, 10) == 0:
                grid_rows += [1]
            else:
                grid_rows += [0]
        grid += [grid_rows]
    return grid


def clear_console():

    if sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("darwin"):
        os.system("clear")
    else:
        print("Platform not supported")
