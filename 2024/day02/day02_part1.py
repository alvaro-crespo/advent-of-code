import os

def count_safe_reports(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Parse the input into a list of lists of int
    reports = []
    for line in lines:
        report = []
        for num in line.split():
            report.append(int(num))
        reports.append(report)

    def is_safe(report):
        # Calculate differences between consecutive levels
        differences = []
        for i in range(len(report) - 1):
            differences.append(report[i + 1] - report[i])

        # Check if all differences are between [1,3], or [-1,-3]
        if not all(1 <= abs(diff) <= 3 for diff in differences):
            return False
        
        # Check if the report is always increasing or decreasing
        increasing = all(diff > 0 for diff in differences)
        decreasing = all(diff < 0 for diff in differences)
        
        return increasing or decreasing

    # Count total safe reports
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
    
    return safe_count


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_02.txt')
    safe_reports_count = count_safe_reports(file_path)
    print(f"The number of safe reports is: {safe_reports_count}")