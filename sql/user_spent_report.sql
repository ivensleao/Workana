SELECT 
    customer_name_customer AS customer_name,
    SUM(amount) AS total_spent
FROM 
    merged_transactions
GROUP BY 
    customer_name_customer
ORDER BY 
    total_spent DESC;