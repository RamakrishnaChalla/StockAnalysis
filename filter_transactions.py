import csv

# filepath: /workspaces/StockAnalysis/filter_transactions.py
# Input and output file paths
input_file = 'transactions_cleaned.csv'
output_file = 'transactions_greater_50000.csv'

# Open the input CSV file for reading
with open(input_file, 'r', encoding='utf-8') as csv_in:
    csv_reader = csv.reader(csv_in)
    rows = list(csv_reader)

# Extract the header and data rows
header = rows[0]
data_rows = rows[1:]

# Find the index of the Amount column
amount_index = header.index("Amount")

# Filter rows where the Amount is less than 100
filtered_rows = [row for row in data_rows if float(row[amount_index]) >= 50000]

# Write the filtered data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerow(header)  # Write the header
    csv_writer.writerows(filtered_rows)  # Write the filtered rows

print(f"Filtered transactions have been saved to {output_file}")