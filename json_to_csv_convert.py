import json
import csv

# filepath: /workspaces/StockAnalysis/json_to_csv_converter.py
# Load the JSON data from the file
input_file = 'transactions.json'
output_file = 'transactions.csv'

with open(input_file, 'r') as json_file:
    data = json.load(json_file)

# Open a CSV file for writing
with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header row (keys from the first dictionary in the JSON array)
    header = data[0].keys()
    csv_writer.writerow(header)

    # Write the data rows
    for transaction in data:
        csv_writer.writerow(transaction.values())

print(f"JSON data has been successfully converted to {output_file}")