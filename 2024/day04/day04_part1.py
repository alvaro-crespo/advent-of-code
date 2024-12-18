import os

# Directions (row, column)
DIRECTIONS = [
    (0, 1),    # Right
    (0, -1),   # Left
    (1, 0),    # Down
    (-1, 0),   # Up
    (1, 1),    # Down-right 
    (1, -1),   # Down-left
    (-1, 1),   # Up-right
    (-1, -1)   # Up-left
]

def count_xmas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    target_len = len(target)
    count = 0
    
    # check word in a direction
    def check_direction(r, c, dr, dc):
        for i in range(target_len):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != target[i]:
                return False
        return True
    
    # traverse each cell
    for r in range(rows):
        for c in range(cols):
            for dr, dc in DIRECTIONS:
                if check_direction(r, c, dr, dc):
                    count += 1
    return count

def load_grid_from_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # non-empty lines
                grid.append(list(line))
    return grid

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_04.txt')
    grid = load_grid_from_file(file_path)
    result = count_xmas_occurrences(grid)
    print(f"Number of times that 'XMAS' appears in the grid: {result}")
