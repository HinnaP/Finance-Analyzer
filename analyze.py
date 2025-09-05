import pandas as pd

# Load data
df = pd.read_csv("transactions.csv")

# Clean columns
df.columns = df.columns.str.strip().str.lower()

=df["date"] = pd.to_datetime(df["date"])

def categorize(description):
    desc = description.lower()
    if "rent" in desc:
        return "Housing"
    elif "starbucks" in desc or "kroger" in desc:
        return "Food & Drink"
    elif "netflix" in desc or "amazon" in desc:
        return "Entertainment"
    elif "uber" in desc or "gas" in desc:
        return "Transport"
    elif "paycheck" in desc:
        return "Income"
    else:
        return "Other"

df["category"] = df["description"].apply(categorize)

print("=== Spending by Category ===")
print(df.groupby("category")["amount"].sum())

# Totals by month
df["month"] = df["date"].dt.to_period("M")
print("\n=== Spending by Month ===")
print(df.groupby("month")["amount"].sum())

print("\n=== Preview ===")
print(df.head())
