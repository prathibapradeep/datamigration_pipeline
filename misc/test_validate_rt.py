import sys
import os
from google.cloud import bigquery

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../pipeline')))
from validate import parse_customer, parse_transaction  # type: ignore


# Setup BigQuery client 
client = bigquery.Client()

def test_customers_from_bq():
    # Query the customer table
    query = """
    SELECT 
        CAST(customer_id AS STRING) || ',' || first_name || ',' || last_name || ',' || email || ',' || FORMAT_DATE('%Y-%m-%d', created_at) AS raw_line
    FROM `datamigration-ct-463114.ds_datamigration_ct.customers`
    LIMIT 10
    """
    results = client.query(query).result()

    for row in results:
        raw_line = row.raw_line
        parsed = parse_customer(raw_line)
        # assertions:
        assert isinstance(parsed["customer_id"], int)
        assert isinstance(parsed["first_name"], str)
        assert "@" in parsed["email"]
       


def test_transactions_from_bq():
    # Query the transactions table 
    query = """
    SELECT 
        CAST(transaction_id AS STRING) || ',' || CAST(customer_id AS STRING) || ',' || CAST(amount AS STRING) || ',' || FORMAT_DATE('%Y-%m-%d', transaction_date) AS raw_line
    FROM `datamigration-ct-463114.ds_datamigration_ct.transactions`
    LIMIT 10
    """
    results = client.query(query).result()

    for row in results:
        raw_line = row.raw_line
        parsed = parse_transaction(raw_line)
        # assertions:
        assert isinstance(parsed["transaction_id"], int)
        assert isinstance(parsed["amount"], float)
        assert parsed["amount"] >= 0
        