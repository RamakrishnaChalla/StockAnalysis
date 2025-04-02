import re
import json

def parse_transaction_data(data):
    transactions = []
    transaction_pattern = re.compile(
        r"(?P<Date>[A-Za-z]{3} \d{2}, \d{4})\n"
        r"(?P<Time>\d{2}:\d{2} (?:am|pm))\n"
        r"(?P<Transaction_Details>.+?)\s(?P<Type>DEBIT|CREDIT)\s₹(?P<Amount>[0-9,]+(?:\.\d{2})?)\n"
        r"Transaction ID (?P<Transaction_ID>\w+)\n"
        r"UTR No\. (?P<UTR_No>\w+)\n"
        r"(Paid by|Credited to) (?P<Account>\w+)"
    )

    for match in transaction_pattern.finditer(data):
        transaction = match.groupdict()
        transaction["Amount"] = float(transaction["Amount"].replace(",", ""))
        transactions.append(transaction)

    return transactions

def main():
    # Load the transaction data from the file
    with open("transaction_data.txt", "r") as file:
        data = file.read()

    # Parse the transaction data
    transactions = parse_transaction_data(data)

    # Convert to JSON
    with open("transactions.json", "w") as json_file:
        json.dump(transactions, json_file, indent=4)

    print("Transactions have been successfully converted to JSON and saved to 'transactions.json'.")

if __name__ == "__main__":
    main()