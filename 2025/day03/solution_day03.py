from pathlib import Path

def part_1(banks):

    output = 0

    for bank in banks:
        xo, xf = 0, 0
        i = 0
        index = 0
        for i, digit in enumerate(bank[:-1]):
            if digit > xo:
                xo = digit
                index = i
                if xo == 9:
                    break
        xf = max(bank[index+1:])
        joltage = xo * 10 + xf
        output += joltage
    return output

def part_2(banks):
    output = 0
    for bank in banks:
        k = 12
        drop = len(bank) - k # how many nums we can drop
        stack = []
        # Build the largest subsequence
        for num in bank:
            while drop > 0 and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        digits = stack[:12]
        num = int("".join(str(digit) for digit in digits))
        output += num

    return output

def main():
    root = Path(__file__).parent
    file_path = root / "input_day03.txt"
    banks = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            nums = [int(n) for n in line]
            banks.append(nums)    
    print(f"Part 1: {part_1(banks)}")
    print(f"Part 2: {part_2(banks)}")

if __name__ == "__main__":
    main()
