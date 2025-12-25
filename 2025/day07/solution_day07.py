def part_1(raw_lines) -> int:
    start_col = next(i for i, ch in enumerate(raw_lines[0]) if ch == "S")
    beams = {start_col} # set with the indexes from where we start a beam downstream
    splits = 0
    # loop over lines downstream, and loop over beams
    for r in range(1, len(raw_lines)):
        next_beams = set()
        width = len(raw_lines[r])
        for beam in beams:
            if raw_lines[r][beam] == ".":
                next_beams.add(beam)
            elif raw_lines[r][beam] == "^":
                if beam + 1 <= width:
                    next_beams.add(beam+1)
                if beam -1 >= 0:
                    next_beams.add(beam-1)
                splits += 1
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
            raw_lines.append(line.rstrip("\n"))
    print(f"Part 1: {part_1(raw_lines = raw_lines)}")
    print(f"Part 2: {part_2(raw_lines = raw_lines)}")


if __name__ == "__main__":
    main()
