import csv
from collections import defaultdict

# Input and output file paths
input_file = 'transactions_cleaned.csv'
output_file = 'transactions_grouped_50000.csv'

# Dictionary to store grouped data
grouped_data = defaultdict(float)

# Open the input CSV file for reading
with open(input_file, 'r', encoding='utf-8') as csv_in:
    csv_reader = csv.reader(csv_in)
    header = next(csv_reader)  # Read the header row

    # Find the indices of relevant columns
    transaction_details_index = header.index("Transaction_Details")
    amount_index = header.index("Amount")

    # Group transactions by Transaction_Details
    for row in csv_reader:
        transaction_details = row[transaction_details_index]
        # Convert Amount to float and add to the grouped data
        try:
            amount = float(row[amount_index])
            #if amount >= 50000:
                # Only include transactions with Amount > 50000
                # Use a tuple to group by Transaction_Details and Amount
            grouped_data[transaction_details] += amount
        except ValueError:
            print(f"Skipping invalid amount: {row[amount_index]} in row: {row}")

# Write the grouped data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerow(["Transaction_Details", "Total_Amount"])  # Write the header

    # Write grouped data
    for transaction_details, total_amount in grouped_data.items():
        csv_writer.writerow([transaction_details, total_amount])

print(f"Grouped transactions have been saved to {output_file}")