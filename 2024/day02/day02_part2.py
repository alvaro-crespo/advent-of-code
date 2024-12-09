import os

def count_safe_reports_with_dampener(file_path):

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
        
        # Check if report is always increasing or decreasing
        increasing = all(diff > 0 for diff in differences)
        decreasing = all(diff < 0 for diff in differences)
        
        return increasing or decreasing

    def is_safe_with_dampener(report):
        # Check if report already safe
        if is_safe(report):
            return True
        
        # Remove each level and check if remaining report is safe
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1:]  # Remove the i-th level
            if is_safe(new_report):
                return True
        
        return False

    # Count total safe reports considering the Problem dampener
    total_safe_reports = 0
    for report in reports:
        if is_safe_with_dampener(report):
            total_safe_reports += 1
    
    return total_safe_reports


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'input_day_02.txt')
    total_safe_reports = count_safe_reports_with_dampener(file_path)
    print(f"The number of safe reports with the Problem Dampener is: {total_safe_reports}")