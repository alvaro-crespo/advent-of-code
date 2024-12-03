import os

def calculate_similarity_score(file_path):
    # Read input file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Parse the two columns into separate lists
    left_list = []
    right_list = []
    for line in lines:
        split_line = line.split()
        left, right = int(split_line[0]), int(split_line[1])
        left_list.append(left)
        right_list.append(right)
    
    # Count occurrences of each number in right list
    right_counts = {}
    for num in right_list:
        if num in right_counts:
            right_counts[num] += 1
        else:
            right_counts[num] = 1
    
    # Calculate similarity score with the left list
    similarity_score = 0
    for num in left_list:
        if num in right_counts:
            similarity_score += num * right_counts[num]
    
    return similarity_score



if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_01.txt')
    similarity_score = calculate_similarity_score(file_path)
    print(f"The similarity score is: {similarity_score}")