import sys, json, argparse
import pandas as pd
from pathlib import Path
from typing import Dict, Callable

def load_rules(path: Path) -> Dict[str, list]:
    if not path.exists():
        return {"Other": []}
    return json.loads(path.read_text())

def categorize_factory(rules: Dict[str, list]) -> Callable[[str], str]:
    rules_lc = {cat: [k.lower() for k in kws] for cat, kws in rules.items()}
    def categorize(desc: str) -> str:
        d = str(desc).lower()
        for cat, kws in rules_lc.items():
            if any(k in d for k in kws):
                return cat
        return "Other"
    return categorize

def run_analysis(csv_path: Path, rules_path: Path, outdir: Path, preview_rows: int = 10) -> None:
    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        sys.exit(1)
    outdir.mkdir(parents=True, exist_ok=True)

    rules = load_rules(rules_path)
    categorize = categorize_factory(rules)

    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip().str.lower()
    if "description" not in df.columns:
        for alt in ["details", "desc", "merchant"]:
            if alt in df.columns:
                df.rename(columns={alt: "description"}, inplace=True)
                break
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "description", "amount"]).copy()
    df["category"] = df["description"].apply(categorize)
    df["month"] = df["date"].dt.to_period("M")

    expenses = df[df["amount"] < 0]
    income   = df[df["amount"] > 0]

    print(f"=== Rows === {len(df)}\n")

    cat_spend = (expenses.groupby("category")["amount"].sum().sort_values())
    print("=== Spending by Category (Expenses only) ===")
    print(cat_spend.to_string() if not cat_spend.empty else "No expenses found.")
    cat_spend.to_csv(outdir / "spending_by_category.csv")

    net_by_month = df.groupby("month")["amount"].sum().sort_index()
    print("\n=== Net by Month (Income + Expenses) ===")
    print(net_by_month.to_string() if not net_by_month.empty else "No data.")
    net_by_month.to_csv(outdir / "net_by_month.csv")

    top_merchants = (expenses.groupby("description")["amount"].sum().sort_values().head(10))
    print("\n=== Top 10 Merchants by Spend ===")
    print(top_merchants.to_string() if not top_merchants.empty else "No expenses found.")
    top_merchants.to_csv(outdir / "top_merchants.csv")

    print("\n=== Preview ===")
    print(df.head(preview_rows).to_string(index=False))

    df.to_csv(outdir / "transactions_enriched.csv", index=False)
    print(f"\nWrote summaries to {outdir}")

def main():
    ap = argparse.ArgumentParser(description="Analyze finance transactions.")
    ap.add_argument("csv", nargs="?", default="transactions.csv")
    ap.add_argument("--rules", default="categories.json")
    ap.add_argument("--outdir", default="outputs")
    ap.add_argument("--preview", type=int, default=10)
    args = ap.parse_args()
    run_analysis(Path(args.csv), Path(args.rules), Path(args.outdir), args.preview)

if __name__ == "__main__":
    main()
