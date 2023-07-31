import os
import re

def extract_number_from_line(line):
    numbers = re.findall(r'\d+', line)
    return max(map(int, numbers)) if numbers else 0

def custom_sort(line, sort_by_number=True):
    if sort_by_number:
        return (-extract_number_from_line(line), -len(line))
    else:
        return -len(line)

def sort_file_by_number_and_length(input_file, output_file, sort_by_number=True):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(script_dir, input_file)
    output_file_path = os.path.join(script_dir, output_file)

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    if "*Creation Club:" in ''.join(lines):
        filtered_lines = [line for line in lines if line.strip().startswith("*Creation Club:")]

        sorted_filtered_lines = sorted(filtered_lines, key=lambda line: custom_sort(line, sort_by_number))

        # Replace the sorted lines back to their original positions
        sorted_lines = lines[:]
        index = 0
        for i, line in enumerate(lines):
            if line.strip().startswith("*Creation Club:"):
                sorted_lines[i] = sorted_filtered_lines[index]
                index += 1
    else:
        # If no lines start with "*Creation Club:", keep the original order
        sorted_lines = lines

    with open(output_file_path, 'w') as file:
        file.writelines(sorted_lines)

if __name__ == "__main__":
    print("Sorting Options:")
    print("1. Sort based first on CC numbers and after on phrase length.")
    print("2. Sorting based only on length.")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        sort_by_number = True
    elif choice == 2:
        sort_by_number = False
    else:
        print("Invalid choice. Keeping the sort as it already is.")
        sort_by_number = False

    input_file = 'input.txt'
    output_file = 'output.txt'

    sort_file_by_number_and_length(input_file, output_file, sort_by_number)

    print("Lines sorted as per your choice and written to the output file.")
