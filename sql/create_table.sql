CREATE OR REPLACE TABLE merged_transactions (
    transaction_id INT,
    customer_name_transaction STRING,
    amount DECIMAL(10, 2),
    transaction_date DATE,
    transaction_name STRING,
    matched_customer_name STRING,
    match_score INT,
    customer_id INT,
    customer_name_customer STRING,
    email STRING
);