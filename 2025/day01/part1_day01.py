from pathlib import Path


def part_1(lines: list):
    password = 0
    i_x = 50

    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            i_x = (i_x - distance) % 100
        elif direction == "R":
            i_x = (i_x + distance) % 100
        if i_x == 0:
            password += 1
    return password


def part_2(lines):
    i_x = 50
    password = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        step = -1 if direction == "L" else 1
        # Simulate each click
        for _ in range(distance):
            i_x = (i_x + step) % 100
            if i_x == 0:
                password += 1
    return password


def main():
    # File path
    root = Path(__file__).parent
    file_path = root / "input_day01.txt"
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append(line.strip())

    print(f"Part 1: {part_1(lines)}")
    print(f"Part 2: {part_2(lines)}")


if __name__ == "__main__":
    main()
