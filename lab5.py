def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()


def read_input(filename):
    with open(filename, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f]


def write_output(filename, result):
    with open(filename, 'w') as f:
        f.write(str(result))


def count_islands_with_visualization(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    grid_copy = [row[:] for row in grid]
    island_count = 0

    def dfs(r, c, island_num):
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid_copy[r][c] != 1):
            return

        grid_copy[r][c] = island_num

        dfs(r + 1, c, island_num)
        dfs(r - 1, c, island_num)
        dfs(r, c + 1, island_num)
        dfs(r, c - 1, island_num)

    for r in range(rows):
        for c in range(cols):
            if grid_copy[r][c] == 1:
                island_count += 1
                dfs(r, c, island_count + 1)

    return island_count

grid = read_input("input.txt")

result = count_islands_with_visualization(grid)

print(f"\nКількість островів: {result}")

write_output("output.txt", result)
