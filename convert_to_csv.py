import re
import csv

# File paths
input_file = "/workspaces/StockAnalysis/transaction_data.txt"
output_file = "/workspaces/StockAnalysis/transaction_data.csv"

# Regular expressions to extract transaction details
transaction_pattern = re.compile(
    r"(?P<date>\w{3} \d{1,2}, \d{4})\n"
    r"(?P<time>\d{2}:\d{2} (?:am|pm))\n"
    r"(?P<details>.+?)\n"
    r"(?P<type>DEBIT|CREDIT) ₹(?P<amount>[\d,]+(?:\.\d{2})?)\n"
    r"Transaction ID (?P<transaction_id>\w+)\n"
    r"UTR No\. (?P<utr_no>\w+)\n"
    r"(?:Paid by|Credited to) (?P<account>.+)"
)

# Parse the transaction data
transactions = []
with open(input_file, "r") as file:
    content = file.read()
    matches = transaction_pattern.finditer(content)
    for match in matches:
        transactions.append(match.groupdict())

# Write to CSV
with open(output_file, "w", newline="") as csvfile:
    fieldnames = ["Date", "Time", "Transaction Details", "Type", "Amount", "Transaction ID", "UTR No.", "Account"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for transaction in transactions:
        writer.writerow({
            "Date": transaction["date"],
            "Time": transaction["time"],
            "Transaction Details": transaction["details"],
            "Type": transaction["type"],
            "Amount": transaction["amount"],
            "Transaction ID": transaction["transaction_id"],
            "UTR No.": transaction["utr_no"],
            "Account": transaction["account"]
        })

print(f"Transactions have been successfully written to {output_file}")