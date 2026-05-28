import pandas as pd
import sqlite3

print("Loading data into SQLite database...")

conn = sqlite3.connect("finance.db")

# ── LOAD ALL 3 TABLES ──
df_clean = pd.read_csv("cleaned_stock_data.csv")
df_monthly = pd.read_csv("monthly_summary.csv")
df_anomalies = pd.read_csv("anomalies.csv")

df_clean.to_sql("stock_prices", conn, if_exists="replace", index=False)
df_monthly.to_sql("monthly_summary", conn, if_exists="replace", index=False)
df_anomalies.to_sql("anomalies", conn, if_exists="replace", index=False)

# ── VERIFY ──
print("\n Tables in database:")
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print(tables)

print("\n📊 Sample SQL query — Top 5 anomalies by magnitude:")
query = """
    SELECT Date, Ticker, Close, "Daily_Return_%"
    FROM anomalies
    ORDER BY ABS("Daily_Return_%") DESC
    LIMIT 5
"""
print(pd.read_sql(query, conn))

conn.close()
print("\n Database loaded successfully! finance.db is ready.")