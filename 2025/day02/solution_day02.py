from pathlib import Path


def part_1(data: str):
    """Sum up invalid IDs: those only made by a sequence of digits repeated twice"""
    count = 0
    ids = data.split(",")
    for id in ids:
        id = id.strip('"').split("-")
        initial, final = int(id[0]), int(id[1])
        for i in range(initial, final + 1):
            str_i = str(i)
            if len(str_i) % 2 != 0:
                continue
            half = len(str_i) // 2
            if str_i[:half] == str_i[half:]:
                count += i
    return count


def part_2(data: str):
    count = 0
    ids = data.split(",")
    for id in ids:
        id = id.strip('"').split("-")
        start = int(id[0])
        end = int(id[1])
        for i in range(start, end + 1):
            str_i = str(i)
            n = len(str_i)

            for length in range(1, n // 2 + 1):
                potential_pattern = str_i[:length]
                repeated_string = potential_pattern * (n // length)
                if repeated_string == str_i:
                    count += i
                    break
    return count


def main():
    root = Path(__file__).parent
    file_path = root / "input_day02.txt"
    with open(file_path) as f:
        data = f.read()
    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
