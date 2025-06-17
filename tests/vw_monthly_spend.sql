CREATE OR REPLACE VIEW monthly_spend AS
SELECT
  customer_id,
  FORMAT_TIMESTAMP('%Y-%m', transaction_date) AS month,
  SUM(amount) AS total_spend,
  AVG(amount) AS avg_spend
FROM `b_datamigration-ct:ds_datamigration_ct.transactions`
GROUP BY customer_id, month;
