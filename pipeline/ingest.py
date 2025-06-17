
import apache_beam as beam # type: ignore
from apache_beam.options.pipeline_options import PipelineOptions # type: ignore
from pipeline.validate import parse_customer, parse_transaction

def run():
  options = PipelineOptions()
  with beam.Pipeline(options=options) as p:
        (p
         | "ReadCustomers" >> beam.io.ReadFromText("C:/datamigration_pipeline/pipeline/customers.csv", skip_header_lines=1)
         | "ParseCust" >> beam.Map(parse_customer)
         | "LogCust" >> beam.Map(print)
         | "ToBQcust" >> beam.io.WriteToBigQuery(
             "datamigration-ct:ds_datamigration_ct.customers",
             schema="customer_id:INT64,first_name:STRING,last_name:STRING,email:STRING,created_at:DATE",
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
         ))

        (p
         | "ReadTxns" >> beam.io.ReadFromText("C:/datamigration_pipeline/pipeline/transactions.csv", skip_header_lines=1)
         | "ParseTxn" >> beam.Map(parse_transaction)
         | "LogTxn" >> beam.Map(print)
         | "ToBQtxn" >> beam.io.WriteToBigQuery(
             "datamigration-ct:ds_datamigration_ct.transactions",
             schema="transaction_id:INT64,customer_id:INT64,amount:FLOAT,transaction_date:DATE",
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
         ))

if __name__ == "__main__":
    run()    