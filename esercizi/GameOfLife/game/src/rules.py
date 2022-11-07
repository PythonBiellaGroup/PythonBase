def get_live_neighbors(row, col, rows, cols, grid):

    lifes = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                lifes += grid[((row + i) % rows)][((col + j) % cols)]
    return lifes


def grid_changing(rows, cols, grid, next_grid):

    for row in range(rows):
        for col in range(cols):
            if not grid[row][col] == next_grid[row][col]:
                return True
    return False


def create_next_grid(rows, cols, grid, next_grid):

    for row in range(rows):
        for col in range(cols):
            live_cells = get_live_neighbors(row, col, rows, cols, grid)

            # regole
            if live_cells < 2 or live_cells > 3:
                next_grid[row][col] = 0

            elif live_cells == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1

            # elif live_cells >= 2 and live_cells <= 3:
            #     next_grid[row][col] = 1

            else:
                next_grid[row][col] = grid[row][col]
