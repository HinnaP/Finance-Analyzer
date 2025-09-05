import argparse
import csv
import random
from datetime import datetime, timedelta
import numpy as np

CATEGORIES = {
    "Housing": [("Rent Payment", -1200, -1800, "monthly")],
    "Utilities": [("Electric Bill", -60, -140, "monthly"),
                  ("Water Bill", -25, -60, "monthly"),
                  ("Internet Bill", -40, -90, "monthly")],
    "Food & Drink": [("Kroger Groceries", -40, -120, "weekly"),
                     ("Costco", -60, -200, "biweekly"),
                     ("Starbucks", -3, -9, "random"),
                     ("Chipotle", -8, -18, "random")],
    "Transport": [("Gas Station", -30, -80, "weekly"),
                  ("Uber", -8, -35, "random")],
    "Entertainment": [("Netflix Subscription", -13, -18, "monthly"),
                      ("Spotify", -8, -12, "monthly"),
                      ("Amazon", -15, -200, "random"),
                      ("Movie Theater", -10, -25, "random")],
    "Shopping": [("Target", -15, -150, "random"),
                 ("Walmart", -10, -120, "random")],
    "Health": [("CVS Pharmacy", -8, -80, "random"),
               ("Gym Membership", -20, -60, "monthly")],
    "Income": [("Paycheck", 1600, 2600, "biweekly")],
    "Other": [("Misc Purchase", -5, -60, "random")]
}

FREQUENCY_WEIGHTS = {
    "monthly": 1.0,
    "biweekly": 2.0,
    "weekly": 4.0,
    "random": 8.0
}

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def jitter(amount):
    # add small noise to amounts so values differ
    return float(np.round(amount + np.random.normal(0, abs(amount)*0.05), 2))
