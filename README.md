# DATAMIGRATION_PIPELINE
Data Migration using GCP & Beam

**📂 Architecture Overview**: 

GCS → Dataflow (Beam) → BigQuery.

**✅ Prerequisites:**

- Google Cloud SDK installed and authenticated.
- Python 3.8+ and pip installed.
- Enable APIs:
- Dataflow
- BigQuery
- Cloud Storage
- Required permissions on GCS and BigQuery.

**⚙️ Setup Instructions**:
  - Ensure GCP project with required APIs enabled
  - Run Terraform to create infra
  - Install Python dependencies
  - Submit Dataflow job or run Beam locally

**Assumptions**:
  - Input CSVs are clean and use consistent schema
  - Basic IAM roles suffice for prototype
  - Permissions: bucket reader + BigQuery data editor.

**✅ Future Improvements**:
  - Add data quality checks with Deequ or Great Expectations
  - Add streaming ingestion with Pub/Sub.
  - Alerting and monitoring via Cloud Monitoring
  - Scale storage via partitioned/clustering in BQ tables and views.

  
# DETAILED STEPS

**Step 1: Set Up GCP Environment**
1. Create a GCP Project (Datamigration-CT datamigration-ct-463114)
    - Enable API's
    - Authenticate CLI
    - Set the Project and Region
    - IAM (Grant the necessary roles)
2. Create Google Storage Bucket datamigration-ct

**Step 2: Data Ingestion & Storage**

1. Simulate Data (Create two CSV files)
    - customers.csv
    - transactions.csv
2. Use GCP console to upload the above 2 files into the datamigration-ct bucket

**Step 3: Create a Big Query dataset and table**

1. Create a dataset ds_datamigration_ct
2. Create a table customers
    1. Partition by created_at
    2. Cluster by customer_id
3. Create a table transactions
    1. Partition by transaction_date
    2. Cluster by customer_id

**Step 4: Deploy Infrastructure with Terraform**

1. Initialize Terraform
2. Apply Terraform to create Big Query dataset and GCS Bucket

**Step 5: Run Apache Beam (Dataflow) Pipeline**
1. Install Python dependencies
2. Run pipeline on Dataflow

**Step 6: Create Analytical Views in BigQuery**
1. Monthly spend per customer view
2.Top 5% customers by Lifetime value

**Step 7: Run Tests & CI Pipeline (GitHub)**
1. Push your code to GitHub
2. GitHub Actions workflow (.github/workflows/ci.yml) runs on every push.
It:
 -Installs dependencies
 -Runs unit tests from tests/test_validate.py

⚙️ **Notes**:

- Use a setup.py in your pipeline directory if your code has dependencies.
- For a minimal local run during development, switch to --runner=DirectRunner.
