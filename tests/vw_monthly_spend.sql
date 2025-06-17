CREATE OR REPLACE VIEW `datamigration-ct-463114.ds_datamigration_ct.vw_monthly_spend` AS
SELECT
  customer_id,
  FORMAT_TIMESTAMP('%Y-%m', transaction_date) AS month,
  SUM(amount) AS total_spend,
  AVG(amount) AS avg_spend
FROM `datamigration-ct-463114.ds_datamigration_ct.transactions`
GROUP BY customer_id, month;