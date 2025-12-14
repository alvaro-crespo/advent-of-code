from pathlib import Path


def part_1(grid: list):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]
    result = 0

    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch != "@":
                continue

            adj_roles = 0

            for di, dj in directions:
                next_i = i + di
                next_j = j + dj
                if 0 <= next_i < len(grid) and 0 <= next_j < len(line):
                    if grid[next_i][next_j] == "@":
                        adj_roles += 1

            if adj_roles < 4:
                result += 1
    return result


def part_2(input):
    return ""


def main():
    root = Path(__file__).parent
    file_path = root / "input_day04.txt"
    grid = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            grid.append(line)
    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")


if __name__ == "__main__":
    main()
