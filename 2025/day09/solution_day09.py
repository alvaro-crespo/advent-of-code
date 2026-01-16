from pathlib import Path

def parse_points(raw_lines: list[str]) -> list[tuple[int, int]]:
    pts = []
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        x_str, y_str = line.split(",")
        pts.append((int(x_str), int(y_str)))
    return pts
# O(n²) 
def part_1(raw_lines: list[str]) -> int:
    pts = parse_points(raw_lines)
    max_area = 0

    for i in range(len(pts)):
        x1, y1 = pts[i]
        for j in range(i + 1, len(pts)):
            x2, y2 = pts[j]
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            if area > max_area:
                max_area = area
    return max_area

def main() -> None:
    root = Path(__file__).parent
    file_path = root / "input_day09.txt"
    raw_lines = file_path.read_text().splitlines()
    print("Part 1:", part_1(raw_lines))

if __name__ == "__main__":
    main()
