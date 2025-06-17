from google.cloud import bigquery
from google.cloud import storage  # Optional, remove if unused

client = bigquery.Client()
table_id = "datamigration-ct-463114.ds_datamigration_ct.customers"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    schema=[
        bigquery.SchemaField("customer_id", "INTEGER"),
        bigquery.SchemaField("first_name", "STRING"),
        bigquery.SchemaField("last_name", "STRING"),
        bigquery.SchemaField("email", "STRING"),
        bigquery.SchemaField("created_at", "DATE"),
    ],
    skip_leading_rows=1,
)

uri = "gs://b_datamigration-ct/customers.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)

load_job.result()  # Waits for the job to complete

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))