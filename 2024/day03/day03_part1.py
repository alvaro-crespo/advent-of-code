import re
import os

def sum_valid_multiplications(file_path):
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()
    
    # Define the regex to match valid mul(X,Y) instructions
    mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    
    # Find all matches of the valid instructions
    matches = re.findall(mul_pattern, corrupted_memory)
    
    # Calculate the sum of the results of valid multiplications
    total_sum = 0

    # using map function
    # for match in matches:
    #     x, y = map(int, match)
    #     total_sum += x * y
    
    # return total_sum
    
    for match in matches:
        # Convert elements to integers
        x = int(match[0])
        y = int(match[1])
        
        # Add the multiplication of the elements
        total_sum += x * y

    return total_sum

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_03.txt')
    result = sum_valid_multiplications(file_path)
    print(f"The sum of all valid multiplications is: {result}")