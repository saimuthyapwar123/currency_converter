import logging
import json
import os

# -------------Logger Configuration----------------

LOG_DIR = "app/data/logs"
LOG_FILE = "app/data/logs/converter.log"

def get_logger(name):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(name)s - Line:%(lineno)d - %(message)s')
    file_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(file_handler)
    
    return logger


# -------------- Helper Method --------------

DATA_DIR = "app/data/data_json"
DATA_FILE = os.path.join(DATA_DIR, "conversion_history.json")

# ---------------- Helper Functions ----------------

def load_json_data():
    """Load data from a JSON file. Returns empty list if file is missing or invalid."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_json_data(filepath, data):
    """Save data to a JSON file with pretty formatting."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

# ---------------- Main Logic ----------------

def save_conversion_record(amount, from_currency, to_currency, result):
    """Save a currency conversion record to the JSON history file."""
    record = {
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
        "converted_amount": result
    }

    # Ensure the directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    # Load existing data
    data = load_json_data(DATA_FILE)

    # Append new record
    data.append(record)

    # Save updated data
    save_json_data(DATA_FILE, data)
