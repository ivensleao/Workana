SELECT 
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(amount) AS total_spent,
    COUNT(transaction_id) AS total_transactions
FROM 
    merged_transactions
GROUP BY 
    DATE_TRUNC('month', transaction_date)
ORDER BY 
    month;
