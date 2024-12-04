def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid


def search_word(grid, word):
    def check_direction(x, y, dx, dy, word):
        for i in range(len(word)):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True

    def count_in_all_directions(x, y):
        count = 0
        directions = [  # (dX, dY)
            (0, 1), (1, 0), (1, 1), (1, -1),
            (0, -1), (-1, 0), (-1, -1), (-1, 1)
        ]
        for dx, dy in directions:
            if check_direction(x, y, dx, dy, word):
                count += 1
        return count

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count += count_in_all_directions(row, col)
    return count



word_to_search = "XMAS"
grid = read_grid('input.txt')
occurrences = search_word(grid, word_to_search)
print(f"The word '{word_to_search}' appears {occurrences} times.")
