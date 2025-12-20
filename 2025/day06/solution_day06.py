from pathlib import Path
from math import prod


def part_1(raw_lines: list) -> int:
    lines = []
    for line in raw_lines:
        line = line.split()
        # Get all problems elements
        if line[0].isdigit():
            lines.append([int(num) for num in line])
        # Get operations
        else:
            lines.append(line)

    total = 0
    # Compute result per problem and add it to the total
    for i in range(len(lines[1])):
        operation = lines[-1][i]
        if operation == "+":
            problem = 0
            for line in lines[:-1]:
                problem += line[i]
        elif operation == "*":
            problem = 1
            for line in lines[:-1]:
                problem *= line[i]
        total += problem
    return total


def part_2(raw_lines: list[str]) -> int:

    height = len(raw_lines)
    width = max(len(line) for line in raw_lines)

    # Build column strings from top to bottom
    col_strings = []
    for c in range(width):
        col = []
        for r in range(height):
            line = raw_lines[r]
            col.append(line[c] if c < len(line) else " ")  # missing ch as spaces
        col_strings.append("".join(col))

    def parse_number_from_column(col: str) -> int | None:
        # Parse digits top-to-bottom; ignore spaces.
        digits = [ch for ch in col if ch.isdigit()]
        return int("".join(digits)) if digits else None

    total = 0
    i = width - 1  # start at rightmost column

    while i >= 0:
        # Skip separation columns with all spaces
        if col_strings[i].strip() == "":
            i -= 1
            continue

        # Collect one problem, one vertical line of the column string
        block = []
        while i >= 0 and col_strings[i].strip() != "":
            block.append(col_strings[i])
            i -= 1

        # Compute result per problem
        op = None
        nums = []
        for col in block:
            bottom = col[-1]
            if bottom in {"+", "*"}:
                op = bottom
                n = parse_number_from_column(col[:-1])  # exclude operator from digits
                nums.append(n)
            else:
                n = parse_number_from_column(col)
                nums.append(n)
        if op == "+":
            res_col = sum(nums)
        else:
            res_col = prod(nums)
        total += res_col

    return total


def main():
    root = Path(__file__).parent
    file_path = root / "input_day06.txt"

    with open(file_path, "r") as f:
        raw_lines = [line.rstrip("\n") for line in f]

    print(f"Part 1: {part_1(raw_lines = raw_lines)}")
    print(f"Part 2: {part_2(raw_lines = raw_lines)}")


if __name__ == "__main__":
    main()
