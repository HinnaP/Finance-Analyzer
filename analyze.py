import sys
import json
import pandas as pd
from pathlib import Path

# Load category rules from JSON
with open("categories.json", "r") as f:
    category_rules = json.load(f)

def categorize(description):
    """Assign a category based on description text and rules in categories.json"""
    desc = str(description).lower()
    for category, keywords in category_rules.items():
        if any(keyword in desc for keyword in keywords):
            return category
    return "Other"

def main():
    # Pick file from CLI or default to transactions.csv
    filename = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("transactions.csv")
    if not filename.exists():
        print(f"File not found: {filename}")
        sys.exit(1)

    # Load data
    df = pd.read_csv(filename)
    df.columns = df.columns.str.strip().str.lower()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "description", "amount"])

    # Categorize transactions
    df["category"] = df["description"].apply(categorize)
    df["month"] = df["date"].dt.to_period("M")

    # Expenses (negative amounts)
    expenses = df[df["amount"] < 0]
    income = df[df["amount"] > 0]

    print("=== Rows ===", len(df))
    print()

    print("=== Spending by Category (Expenses only) ===")
    cat_spend = (expenses.groupby("category")["amount"]
                 .sum()
                 .sort_values())
    print(cat_spend.to_string())
    print()

    print("=== Net by Month (Income + Expenses) ===")
    net_by_month = (df.groupby("month")["amount"]
                    .sum()
                    .sort_index())
    print(net_by_month.to_string())
    print()

    print("=== Top 10 Merchants by Spend ===")
    merch_spend = (expenses.groupby("description")["amount"]
                   .sum()
                   .sort_values()
                   .head(10))
    print(merch_spend.to_string())
    print()

    print("=== Preview ===")
    print(df.head(10).to_string(index=False))

if __name__ == "__main__":
    main()
