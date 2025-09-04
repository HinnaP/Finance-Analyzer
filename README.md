# 💰 Finance Analyzer

A web app that analyzes personal finance data, categorizes expenses, and visualizes spending trends.  

---

## 🖥 How to Use

### 1. Clone the repository
```bash
git clone https://github.com/HinnaP/Finance-Analyzer.git
cd Finance-Analyzer
2. Create a virtual environment
Windows (PowerShell):

powershell
Copy code
py -m venv venv
venv\Scripts\Activate
macOS/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
bash
Copy code
pip install -r requirements.txt

4. Run the app
bash
Copy code
python app.py
Then open your browser and go to:
👉 http://127.0.0.1:5000

Features
Upload CSV files (e.g., bank or credit card statements)

Automatic data cleaning and column normalization

Rule-based expense categorization (Food, Rent, Entertainment, etc.)

Interactive dashboards with:

Monthly spending trends

Category breakdowns

Top recurring expenses

Exportable insights for budgeting and savings goals

Tech Stack
Backend
Python (Flask)
Pandas
SQLAlchemy (SQLite/PostgreSQL)

Frontend
HTML, CSS, JavaScript
Chart.js (data visualization)

Other
Docker (for deployment, planned)
Power BI integration (optional, future)
GitHub Actions (for CI/CD, future)

Project Structure

Finance-Analyzer/
│
├── app.py              # Flask app entry point
├── requirements.txt    # Dependencies
├── templates/          # HTML templates
├── static/             # CSS/JS assets
├── data/               # Uploaded CSVs
└── README.md           # Project documentation
