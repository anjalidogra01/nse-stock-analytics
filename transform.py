import pandas as pd

df = pd.read_csv("raw_stock_data.csv")

print("Starting data transformation & validation...")

# ── 1. FIX DATA TYPES ──
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

# ── 2. VALIDATE — check for nulls ──
null_count = df.isnull().sum().sum()
print(f"Null values found: {null_count}")
df.dropna(subset=["Close", "Volume"], inplace=True)

# ── 3. DAILY RETURN — % change per day ──
df = df.sort_values(["Ticker", "Date"])
df["Daily_Return_%"] = df.groupby("Ticker")["Close"].pct_change() * 100
df["Daily_Return_%"] = df["Daily_Return_%"].round(2)

# ── 4. ANOMALY DETECTION — flag unusual price movements ──
threshold = 3.0  # more than 3% move in a day = anomaly
df["Is_Anomaly"] = df["Daily_Return_%"].abs() > threshold
anomalies = df[df["Is_Anomaly"] == True]
print(f"Anomalies detected (moves > {threshold}%): {len(anomalies)}")

# ── 5. MONTHLY SUMMARY ──
df["Month"] = df["Date"].dt.to_period("M")
monthly = df.groupby(["Ticker", "Month"]).agg(
    Avg_Close=("Close", "mean"),
    Max_Close=("Close", "max"),
    Min_Close=("Close", "min"),
    Total_Volume=("Volume", "sum")
).reset_index()
monthly["Month"] = monthly["Month"].astype(str)
monthly["Avg_Close"] = monthly["Avg_Close"].round(2)

# ── 6. SAVE ──
df.to_csv("cleaned_stock_data.csv", index=False)
monthly.to_csv("monthly_summary.csv", index=False)
anomalies.to_csv("anomalies.csv", index=False)

print(f"✅ Transformation complete!")
print(f"Clean rows: {len(df)}")
print(f"Monthly summaries: {len(monthly)}")
print(f"\nSample anomalies:")
print(anomalies[["Date", "Ticker", "Close", "Daily_Return_%"]].head())