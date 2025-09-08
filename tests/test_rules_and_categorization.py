import json
from pathlib import Path
from analyze import load_rules, categorize_factory

def test_categories_json_exists():
    p = Path("categories.json")
    assert p.exists(), "categories.json should exist at project root"

def test_categorization_food_drink():
    rules = load_rules(Path("categories.json"))
    categorize = categorize_factory(rules)
    assert categorize("Starbucks Coffee") in {"Food & Drink", "Other"}
