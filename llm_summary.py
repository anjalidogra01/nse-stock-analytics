import pandas as pd
from google import genai

# ── CONFIGURE GEMINI ──
client = genai.Client(api_key="GEMINI_API_KEY")
for model in client.models.list():
    print(model.name)
# ── LOAD DATA ──
anomalies = pd.read_csv("anomalies.csv")

# ── PREPARE CONTEXT ──
top_anomalies = anomalies.nlargest(5, "Daily_Return_%")[["Date","Ticker","Close","Daily_Return_%"]]
bottom_anomalies = anomalies.nsmallest(5, "Daily_Return_%")[["Date","Ticker","Close","Daily_Return_%"]]

prompt = f"""
You are a financial analyst assistant. Analyze this Indian stock market data and write a 
concise professional summary report (max 150 words).

TOP POSITIVE ANOMALIES (biggest single-day gains):
{top_anomalies.to_string(index=False)}

TOP NEGATIVE ANOMALIES (biggest single-day crashes):
{bottom_anomalies.to_string(index=False)}

Include:
1. Key observations about which stocks were most volatile
2. Any patterns you notice
3. Risk assessment in one line
Keep it professional, like a finance report.
"""

print("Sending data to Gemini API...")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

summary = response.text
print("\n AI-GENERATED FINANCIAL SUMMARY:")
print("="*50)
print(summary)
print("="*50)

with open("financial_summary.txt", "w") as f:
    f.write(summary)

print("\n Summary saved to financial_summary.txt")