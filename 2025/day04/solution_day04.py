from pathlib import Path


DIRECTIONS = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
)


def part_1(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    result = 0

    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch != "@":
                continue

            adj_rolls = 0

            for di, dj in DIRECTIONS:
                next_i = i + di
                next_j = j + dj
                if (
                    0 <= next_i < rows
                    and 0 <= next_j < cols
                    and grid[next_i][next_j] == "@"
                ):
                    adj_rolls += 1
                    if adj_rolls == 4:
                        break
            if adj_rolls < 4:
                result += 1
    return result


def part_2(grid: list[str]) -> int:
    grid = [list(row) for row in grid]
    rows = len(grid)
    cols = len(grid[0])
    removed = 0

    # Continue until no more rolls can be removed
    while True:
        remove_i = []
        for i, line in enumerate(grid):
            for j, ch in enumerate(line):
                if ch != "@":
                    continue

                adj_rolls = 0

                for di, dj in DIRECTIONS:
                    next_i = i + di
                    next_j = j + dj
                    if (
                        0 <= next_i < rows
                        and 0 <= next_j < cols
                        and grid[next_i][next_j] == "@"
                    ):
                        adj_rolls += 1
                if adj_rolls < 4:
                    remove_i.append((i, j))
        if not remove_i:
            break
        removed += len(remove_i)
        # Update grid with removed rolls
        for point in remove_i:
            grid[point[0]][point[1]] = "."
    return removed


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
