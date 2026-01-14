from pathlib import Path


def part_1(raw_lines: list[str]) -> int:
    # Parse points
    junctions: list[tuple[int, int, int]] = []
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(","))
        junctions.append((x, y, z))

    n = len(junctions)
    if n == 0:
        return 0
    if n == 1:
        return 1

    def dist2(i: int, j: int) -> int:
        x1, y1, z1 = junctions[i]
        x2, y2, z2 = junctions[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        return dx * dx + dy * dy + dz * dz

    # Find union
    parent = list(range(n))
    size = [1] * n

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> bool:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    # Build all pairs (distance^2, i, j)
    all_pairs: list[tuple[int, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            all_pairs.append((dist2(i, j), i, j))

    # Sorting by distance
    all_pairs.sort(key=lambda t: t[0])

    # Connect 1000 closest pairs
    k = min(1000, len(all_pairs))
    for idx in range(k):
        _, i, j = all_pairs[idx]
        union(i, j)

    # Component sizes
    comp_sizes: dict[int, int] = {}
    for i in range(n):
        r = find(i)
        comp_sizes[r] = size[r]

    top3 = sorted(comp_sizes.values(), reverse=True)[:3]
    return top3[0] * top3[1] * top3[2]


def part_2(raw_lines: list[str]) -> int:
    # Parse points
    junctions: list[tuple[int, int, int]] = []
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(","))
        junctions.append((x, y, z))

    n = len(junctions)
    if n < 2:
        return 0

    def dist2(i: int, j: int) -> int:
        x1, y1, z1 = junctions[i]
        x2, y2, z2 = junctions[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        return dx * dx + dy * dy + dz * dz

    # Union find
    parent = list(range(n))
    size = [1] * n

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> bool:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    # Build and sort all unique pairs
    all_pairs: list[tuple[int, int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            all_pairs.append((dist2(i, j), i, j))
    all_pairs.sort()

    components = n
    for _, i, j in all_pairs:
        if union(i, j):
            components -= 1
            if components == 1:
                return junctions[i][0] * junctions[j][0]


def main() -> None:
    root = Path(__file__).parent
    file_path = root / "input_day08.txt"

    with open(file_path, "r") as f:
        raw_lines = [line.rstrip("\n") for line in f]

    print(f"Part 1: {part_1(raw_lines=raw_lines)}")
    print(f"Part 2: {part_2(raw_lines=raw_lines)}")


if __name__ == "__main__":
    main()
