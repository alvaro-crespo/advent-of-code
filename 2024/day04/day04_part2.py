import os

def count_x_mas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Check word "X-MAS" exists centered at a specific cell
    def has_xmas(r, c):
        if not (1 <= r < rows - 1 and 1 <= c < cols - 1):
            return False
        if grid[r][c] != "A":
            return False

        # Check both diagonals
        d_1 = f"{grid[r-1][c-1]}{grid[r+1][c+1]}"
        d_2 = f"{grid[r-1][c+1]}{grid[r+1][c-1]}"

        return d_1 in ["MS", "SM"] and d_2 in ["MS", "SM"]

    # traverse each cell
    for r in range(rows):
        for c in range(cols):
            count += has_xmas(r, c)
    return count

def load_grid_from_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Non-empty lines
                grid.append(list(line))
    return grid

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_04.txt')
    grid = load_grid_from_file(file_path)
    result = count_x_mas_occurrences(grid)
    print(f"Number of times that 'X-MAS' appears in the grid: {result}")
