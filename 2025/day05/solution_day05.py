from pathlib import Path


def merge_ranges(ranges: list) -> list:
    """Merge overlapping ranges."""
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]

    for [start, end] in ranges[1:]:
        if merged[-1][1] >= start:
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append([start, end])
    return merged


def part_1(ranges: list, ingredients: list[int]) -> int:
    fresh = 0
    merged = merge_ranges(ranges)
    # Check if every ingredient is within fresh IDs ranges
    for ingredient in ingredients:
        for fresh_range in merged:
            if ingredient in range(fresh_range[0], fresh_range[1] + 1):
                fresh += 1
                break
    return fresh


def part_2(ranges) -> int:
    ranges.sort(key=lambda x: x[0])
    merged = merge_ranges(ranges)
    # Get number of fresh ids from each merged range
    fresh = 0
    for fresh_range in merged:
        fresh += fresh_range[1] - fresh_range[0] + 1
    return fresh


def main():
    root = Path(__file__).parent
    file_path = root / "input_day05.txt"
    ranges, ingredients = [], []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if "-" in line:
                i, f = map(int, line.split("-"))
                ranges.append([i, f])
            elif line != "":
                ingredients.append(int(line))
    print(f"Part 1: {part_1(ranges, ingredients)}")
    print(f"Part 2: {part_2(ranges)}")


if __name__ == "__main__":
    main()
