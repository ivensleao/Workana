SELECT 
    customer_name_customer AS customer_name,
    email,
    SUM(amount) AS total_spent
FROM 
    merged_transactions
GROUP BY 
    customer_name_customer, email
ORDER BY 
    total_spent DESC
LIMIT 10;
