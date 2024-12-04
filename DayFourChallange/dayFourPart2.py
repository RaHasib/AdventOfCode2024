def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid


def count_xmas_in_grid(grid):
    max_x, max_y = len(grid), len(grid[0])
    count_xmas = 0

    for x in range(1, max_x - 1):
        for y in range(1, max_y - 1):

            if grid[x][y] == 'A':
                if (
                        ((grid[x - 1][y - 1] == 'M' and grid[x + 1][y + 1] == 'S') or
                         (grid[x - 1][y - 1] == 'S' and grid[x + 1][y + 1] == 'M'))
                ) and (
                        # Diagonal 2: top-right to bottom-left
                        ((grid[x - 1][y + 1] == 'M' and grid[x + 1][y - 1] == 'S') or
                         (grid[x - 1][y + 1] == 'S' and grid[x + 1][y - 1] == 'M'))
                ):
                    count_xmas += 1

    return count_xmas


file_path = 'input.txt'
grid = read_grid(file_path)
xmas_count = count_xmas_in_grid(grid)
print(f"The pattern 'X-MAS' appears {xmas_count} times.")
