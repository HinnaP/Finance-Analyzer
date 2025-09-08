# Finance Analyzer
A Python project that analyzes personal finance data, categorizes expenses, and summarizes spending trends.  

## Requirements
- Python 3.8 or later
- pandas
- numpy

## How to Use

1. Clone the repository
git clone https://github.com/HinnaP/Finance-Analyzer.git
cd Finance-Analyzer

2. Create a virtual environment:
- Windows (PowerShell):
    - py -m venv venv
    - venv\Scripts\Activate

- macOS/Linux:
    - python3 -m venv venv
    - source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Generate sample transactions (optional)
python generate_transactions.py --rows 500 --out transactions.csv

5. Run the analyzer
python analyze.py transactions.csv

``` bash│
├── Project Structure
|
├── analyze.py               # Main analysis script
├── generate_transactions.py # Script to create synthetic CSV data
├── transactions.csv         # Example dataset
├── categories.json          # Category rules
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
