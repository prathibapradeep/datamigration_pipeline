
from pipeline.validate import parse_customer, parse_transaction  # type: ignore

def test_parse_customer():
    rec = parse_customer("1,Jane,Doe,jane@example.com,2021-01-01")
    assert rec["customer_id"] == 1
    assert rec["first_name"] == "Jane"
    assert rec["created_at"] == "2021-01-01"

def test_parse_transaction():
    rec = parse_transaction("100,1,123.45,2024-06-01")
    assert rec["amount"] == 123.45
    assert rec["transaction_date"] == "2024-06-01"
