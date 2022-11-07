import random
import time
from game.src.grid import print_initial_grid, print_grid, clear_console
from game.src.rules import create_next_grid


def run_game(generations: int = 10000):

    clear_console()
    rows = random.randint(10, 60)
    cols = random.randint(10, 118)

    current_grid = print_initial_grid(rows, cols)
    next_grid = print_initial_grid(rows, cols)

    for gen in range(1, generations):

        print_grid(rows, cols, current_grid)
        # applicare le regole alla griglia corrente e passandole a quella successiva
        create_next_grid(rows, cols, current_grid, next_grid)

        time.sleep(1 / 5)

        current_grid, next_grid = next_grid, current_grid
        clear_console()

    print_grid(rows, cols, current_grid)
