from collections import defaultdict

def parse_line(line):
    parts = line.strip().strip('()').split()
    if len(parts) != 6:
        return None
    return parts[1], parts[2], parts[3], parts[4], parts[5]

def count_digits_in_sudoku(input_data):
    row_counts = defaultdict(lambda: defaultdict(int))
    column_counts = defaultdict(lambda: defaultdict(int))
    subgrid_counts = defaultdict(lambda: defaultdict(int))

    # Digits mapping
    digits_mapping = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    # Read file and process each placement
    with open(input_data, 'r') as file:
        for line in file:
            parsed_line = parse_line(line)
            if not parsed_line:
                continue  # Skip lines that don't match the expected format

            digit, _, row, column, subgrid = parsed_line
            digit_val = digits_mapping[digit]

            # Extract row, column, subgrid indices
            row_idx = int(row.replace("row", ""))
            column_idx = int(column.replace("column", ""))
            subgrid_idx = int(subgrid.replace("subgrid", ""))

            # Update counts
            row_counts[row_idx][digit_val] += 1
            column_counts[column_idx][digit_val] += 1
            subgrid_counts[subgrid_idx][digit_val] += 1

    # Convert the counters to regular dictionaries for easier display
    return {k: dict(v) for k, v in row_counts.items()}, \
           {k: dict(v) for k, v in column_counts.items()}, \
           {k: dict(v) for k, v in subgrid_counts.items()}

def check_counts_validity(row_counts, column_counts, subgrid_counts):
    # Check all counts in row_counts
    for row in row_counts.values():
        if not all(count == 1 for count in row.values()):
            return False

    # Check all counts in column_counts
    for column in column_counts.values():
        if not all(count == 1 for count in column.values()):
            return False

    # Check all counts in subgrid_counts
    for subgrid in subgrid_counts.values():
        if not all(count == 1 for count in subgrid.values()):
            return False

    return True


input_data = 'input_data.txt'
row_counts, column_counts, subgrid_counts = count_digits_in_sudoku(input_data)
print("Row Counts:", row_counts)
print("Column Counts:", column_counts)
print("Subgrid Counts:", subgrid_counts)

validity = check_counts_validity(row_counts, column_counts, subgrid_counts)
print("Valid Plan" if validity else "Invalid Plan")