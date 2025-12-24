def part_1(raw_lines) -> int:
    start_col = next(i for i, ch in enumerate(raw_lines[0][0]) if ch == "S")
    splits = 0
    beams = {start_col}

    for r in range(1, len(raw_lines)):
        row = raw_lines[r][0]
        width = len(row)
        next_beams = set()
        for col in beams:
            if not (0 <= col < width):
                continue
            tile = row[col]
            if tile == ".":
                next_beams.add(col)
            elif tile == "^":
                splits += 1
                left = col - 1
                right = col + 1
                if 0 <= left < width:
                    next_beams.add(left)
                if 0 <= right < width:
                    next_beams.add(right)
        beams = next_beams

    return splits


def part_2(raw_lines) -> int:
    return ""


def main():
    from pathlib import Path

    root = Path(__file__).parent
    file_path = root / "input_day07.txt"
    with open(file_path, "r") as f:
        raw_lines = []
        for line in f:
            raw_lines.append(line.split())
    print(f"Part 1: {part_1(raw_lines = raw_lines)}")
    print(f"Part 2: {part_2(raw_lines = raw_lines)}")


if __name__ == "__main__":
    main()
