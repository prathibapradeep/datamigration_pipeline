CREATE OR REPLACE TABLE `datamigration-ct:ds_datamigration_ct.top_customers` AS
WITH customer_ltv AS (
  SELECT
    customer_id,
    SUM(amount) AS lifetime_value,
    RANK() OVER (ORDER BY SUM(amount) DESC) AS rank,
    COUNT(*) OVER () AS total_customers
  FROM
    `datamigration-ct:ds_datamigration_ct.transactions`
  GROUP BY
    customer_id
),
percentile_calc AS (
  SELECT
    *,
    rank * 1.0 / total_customers AS percentile
  FROM customer_ltv
)
SELECT
  customer_id,
  lifetime_value
FROM
  percentile_calc
WHERE
  percentile <= 0.05;