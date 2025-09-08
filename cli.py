import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(prog="finance-analyzer", description="Finance Analyzer CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_an = sub.add_parser("analyze", help="Analyze a transactions CSV")
    p_an.add_argument("csv", nargs="?", default="transactions.csv")
    p_an.add_argument("--rules", default="categories.json")
    p_an.add_argument("--outdir", default="outputs")
    p_an.add_argument("--preview", type=int, default=10)

    p_gen = sub.add_parser("generate", help="Generate synthetic transactions CSV")
    p_gen.add_argument("--rows", type=int, default=500)
    p_gen.add_argument("--start", default="2024-01-01")
    p_gen.add_argument("--end", default="2025-03-31")
    p_gen.add_argument("--out", default="transactions.csv")
    p_gen.add_argument("--seed", type=int, default=42)

    args = parser.parse_args()

    if args.cmd == "analyze":
        from analyze import run_analysis
        run_analysis(Path(args.csv), Path(args.rules), Path(args.outdir), args.preview)
    elif args.cmd == "generate":
        # reuse your existing generator's main
        from generate_transactions import main as gen_main
        # emulate CLI for generator
        import sys
        sys.argv = [
            "generate_transactions.py",
            "--rows", str(args.rows),
            "--start", args.start,
            "--end", args.end,
            "--out", args.out,
            "--seed", str(args.seed),
        ]
        gen_main()

if __name__ == "__main__":
    main()
