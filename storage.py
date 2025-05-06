import json
import os
from datetime import date
import logging

FILE = "tasks.json"

def load_tasks():
    """
    Load tasks from the JSON file. If the file does not exist, return an empty dictionary.
    """
    if not os.path.exists(FILE):
        logging.info(f"{FILE} does not exist. Returning an empty dictionary.")
        return {}
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):  # Ensure the data is in the expected format
                return data
            else:
                logging.warning(f"Unexpected data format in {FILE}. Returning an empty dictionary.")
                return {}
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON from {FILE}. Returning an empty dictionary.")
        return {}
    except Exception as e:
        logging.error(f"An error occurred while loading tasks: {e}")
        return

def save_tasks(all_tasks):
    """
    Save all tasks to the JSON file.
    """
    with open(FILE, "w") as f:
        json.dump(all_tasks, f, indent=2)

def get_today_key():
    """
    Get today's date in ISO format (YYYY-MM-DD).
    """
    return date.today().isoformat()