# Customer Transaction Analysis with BigQuery and Dataflow

## Overview
This project presents a scalable and secure data pipeline prototype on Google Cloud Platform (GCP) for analyzing customer transaction behavior. Designed for a large financial institution migrating to the cloud, the pipeline ingests, transforms, and loads customer and transaction data for analytical insights

🎯 Business Objectives
 - Track customer spending behavior over time
 - Identify high-value customers based on lifetime transaction value

##  Architecture Overview


### 🧱 Components

| Layer              | Technology                     | Description |
|--------------------|-------------------------------|-------------|
| Source             | CSV Files                     | `customers.csv`, `transactions.csv` |
| Storage            | Google Cloud Storage (GCS)    | Raw file storage, staging & temp locations |
| Processing         | Apache Beam on Dataflow       | ETL: clean, transform, validate data |
| Data Warehouse     | BigQuery                      | Analytics-ready tables and views |
| Infrastructure     | Terraform                     | GCP resources provisioning |
| DevOps             | GitHub Actions                | CI for testing transformation logic |
### 🔄 Data Flow Diagram

```text
Local CSV Files
    ↓
Google Cloud Storage
    ↓
Apache Beam (Dataflow)
    ↓
Cleaned Tables in BigQuery
    ↓
SQL Views for Monthly Spend & Top Customers
```

## Setup Instructions:

### 1. Prerequisites:

- Google Cloud SDK installed and authenticated (Enable APIs).
- IAM roles:
    -Storage Admin
    -BigQuery Admin
    -Dataflow Developer
    -Service Account User
- Tools
    - gcloud CLI 
    - Python 3.8+ and pip installed.
    - Terraform
    - Git

### 2. Execution Steps:

1.  **Prepare the GCP Environment**
    -   Create a project (e.g., `datamigration-ct`)
    -   Enable required APIs
    -   Set project and region
    -   Assign IAM roles
    -   Create a Cloud Storage bucket: `datamigration-ct`
        
2.  **Simulate Data & Upload**
    -   Generate `customers.csv` and `transactions.csv`
    -   Upload both to your GCS bucket
        
3.  **Create BigQuery Dataset & Tables**
    -   Dataset: `ds_datamigration_ct`
    -   Table: `customers`
           -   Partitioned by `created_at`, clustered by `customer_id`
    -   Table: `transactions`
           -   Partitioned by `transaction_date`, clustered by `customer_id`
 
4.  **Provision Infrastructure with Terraform**
    -   Initialize Terraform
    -   Apply to provision GCS and BigQuery resources
        
5.  **Run Apache Beam (Dataflow) Pipeline**
    -   Install Python dependencies
    -   Submit job to Dataflow or run locally with `DirectRunner`
        
6.  **Create Analytical Views in BigQuery**
    -   Monthly spend per customer
    -   Top 5% of customers by lifetime transaction value
        
7.  **Set Up CI with GitHub Actions**
    -   Push code to GitHub
    -   Include CI workflow in `.github/workflows/ci.yml`

🛠️ **AdditionalNotes**:
- Use --runner=DirectRunner for local development and testing
- Partitioning and clustering improve query performance and cost.


### Assumptions:
  - Input CSVs are clean and use consistent schema
  - Basic IAM roles suffice for prototype
  - Permissions: bucket reader + BigQuery data editor.




### Future Improvements:
  - Add data quality checks with Deequ or Great Expectations
  - Add streaming ingestion with Pub/Sub.
  - Alerting and monitoring via Cloud Monitoring
  - Scale storage via partitioned/clustering in BQ tables and views.