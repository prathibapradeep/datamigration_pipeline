
provider "google" {
  project = var.project_id
  region  = var.region
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "google_storage_bucket" "data_bucket" {
  name     = "my-data-bucket-${random_id.bucket_suffix.hex}"
  location = "US"
}

resource "google_bigquery_dataset" "analytics" {
  dataset_id = var.bq_dataset
  location   = var.region
}
