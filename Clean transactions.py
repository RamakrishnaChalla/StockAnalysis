import csv

# filepath: /workspaces/StockAnalysis/remove_paid_to.py
# Input and output file paths
input_file = 'transactions.csv'
output_file = 'transactions_cleaned.csv'

# Open the input CSV file for reading
with open(input_file, 'r', encoding='utf-8') as csv_in:
    csv_reader = csv.reader(csv_in)
    rows = list(csv_reader)

# Modify the header and rows
header = rows[0]
data_rows = rows[1:]

# Find the index of the Transaction_Details column
transaction_details_index = header.index("Transaction_Details")
type_index = header.index("Type")
amount_index = header.index("Amount")
transaction_id_index = header.index("Transaction_ID")
utr_no_index = header.index("UTR_No")
account_index = header.index("Account")
date_index = header.index("Date")

# Remove "Paid to" from the Transaction_Details column
for row in data_rows:
    row[transaction_details_index] = row[transaction_details_index].replace("Paid to ", "").replace("Received from ", "")
    if row[type_index].strip().upper() == "DEBIT":
        row[amount_index] = float(row[amount_index])
    else:
        row[amount_index] = 0-float(row[amount_index])

# Write the cleaned data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerow(["Date", "Transaction_Details", "Amount"])  # Write the new header
    for row in data_rows:
        csv_writer.writerow([row[date_index], row[transaction_details_index], row[amount_index]])  # Write selected columns


print(f"Cleaned CSV file has been saved as {output_file}")