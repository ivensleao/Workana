import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    user='snowflake_user',
    password='SUA_SENHA',
    account='ivensleao.snowflakecomputing.com',
    warehouse='workana_dw',
    database='workana_db',
    schema='workana_schema'
)

csv_path = 'data/merged_transactions.csv'
df = pd.read_csv(csv_path)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO merged_transactions (transaction_id, customer_name_transaction, amount, transaction_date, transaction_name, matched_customer_name, match_score, customer_id, customer_name_customer, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

cursor.close()
conn.close()
print("Dados carregados no Snowflake com sucesso!")
