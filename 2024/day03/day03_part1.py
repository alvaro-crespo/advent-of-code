import re
import os

def sum_valid_multiplications(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()
    
    # Define the regular expression to match valid mul(X,Y) instructions
    mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    
    # Find all matches of the valid instructions
    matches = re.findall(mul_pattern, corrupted_memory)
    
    # Calculate the sum of the results of valid multiplications
    total_sum = 0
    for match in matches:
        x, y = map(int, match)  # Convert the captured groups to integers
        total_sum += x * y
    
    return total_sum


if __name__ == "__main__":
    # Adjust the file path to your input file
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_03.txt')
    result = sum_valid_multiplications(file_path)
    print(f"The sum of all valid multiplications is: {result}")