from pathlib import Path


def part_1(input: list) -> int:
    total = 0
    # Compute result per problem and add it to the total
    for i in range(len(input[1])):
        operation = input[-1][i]
        if operation == "+":
            problem = 0
            for line in input[:-1]:
                problem += line[i]
        elif operation == "*":
            problem = 1
            for line in input[:-1]:
                problem *= line[i]
        total += problem
    return total


def part_2(input) -> int:
    return ""


def main():
    root = Path(__file__).parent
    file_path = root / "input_day06.txt"
    with open(file_path) as f:
        lines = []
        for line in f:
            line = line.split()
            # Get all problems elements
            if line[0].isdigit():
                lines.append([int(num) for num in line])
            # Get operations
            else:
                lines.append(line)
    print(f"Part 1: {part_1(input = lines)}")
    print(f"Part 2: {part_2(input = lines)}")


if __name__ == "__main__":
    main()
