import os


def calculate_total_distance(file_path):
    # Read the input file
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Parse the two columns into separate lists
    left_list = []
    right_list = []
    for line in lines:
        split_line = line.split()
        left, right = int(split_line[0]), int(split_line[1])
        left_list.append(left)
        right_list.append(right)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i]-right_list[i])
    
    return total_distance


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_01.txt')
    total_distance = calculate_total_distance(file_path)
    print(f"Total distance: {total_distance}")