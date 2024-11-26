import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

customers = pd.read_csv('data/customers.csv')
transactions = pd.read_csv('data/transactions.csv')

def match_names(customers_df, transactions_df):
    matched_records = []

    for transaction_name in transactions_df['customer_name']:
        best_match = process.extractOne(transaction_name, customers_df['customer_name'], scorer=fuzz.token_sort_ratio)
        
        if best_match and best_match[1] >= 85:  
            matched_records.append((transaction_name, best_match[0], best_match[1]))
        else:
            matched_records.append((transaction_name, None, None))
    
    return pd.DataFrame(matched_records, columns=['transaction_name', 'matched_customer_name', 'match_score'])

matched_results = match_names(customers, transactions)

merged_transactions = transactions.merge(
    matched_results, left_on='customer_name', right_on='transaction_name', how='left'
).merge(
    customers, left_on='matched_customer_name', right_on='customer_name', how='left', suffixes=('_transaction', '_customer')
)

merged_transactions.to_csv('data/merged_transactions.csv', index=False)
