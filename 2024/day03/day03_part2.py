import re
import os

def sum_multiplications_enabled(file_path):

    with open(file_path, 'r') as file:
        corrupted_memory = file.read()

    # Definition of regex patterns
    mult_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Find all instructions occurrences
    instructions = re.findall(rf"({mult_pattern})|({do_pattern})|({dont_pattern})", corrupted_memory)

    total_sum = 0
    enabled = True  # mult instructions enabled by default
    for instruction in instructions:
        # Check which pattern matches
        if instruction[3]:  # do()
            enabled = True
        elif instruction[4]:  # don't()
            enabled = False
        elif instruction[1] and instruction[2]:  # mult(X, Y) 
            if enabled:  # Only process if enabled
                x = int(instruction[1])
                y = int(instruction[2])
                total_sum += x * y
    return total_sum

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_03.txt')
    result = sum_multiplications_enabled(file_path)
    print(f"The sum of all enabled multiplications is: {result}")
