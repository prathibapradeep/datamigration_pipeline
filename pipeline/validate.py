
# validate.py

import datetime

def parse_customer(line):
    fields = line.strip().split(",")
    return {
        "customer_id": int(fields[0]),
        "first_name": fields[1],
        "last_name": fields[2],
        "email": fields[3],
        "created_at": fields[4],  # Format: 'YYYY-MM-DD'
    }

def parse_transaction(line):
    fields = line.strip().split(",")
    return {
        "transaction_id": int(fields[0]),
        "customer_id": int(fields[1]),
        "amount": float(fields[2]),
        "transaction_date": fields[3],  # Format: 'YYYY-MM-DD'
    }