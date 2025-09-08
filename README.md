# Finance Analyzer
A Python project that analyzes personal finance data, categorizes expenses, and summarizes spending trends.  

## Requirements
Python 3.8 or later
pandas
numpy

## How to Use

### 1. Clone the repository
```bash
git clone https://github.com/HinnaP/Finance-Analyzer.git
cd Finance-Analyzer

### 2. Create a virtual environment
For Windows (PowerShell):
py - m venv venv
venv\Scripts\Activate

For macOS/Linus:
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Generate or Provide transactions
python generate_transactions.py --rows 500 --out transactions.csv

### 5. Run the Analyzer
python analyze.py transactions.csv
