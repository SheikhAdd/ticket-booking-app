import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"tickets": [], "hall_state": {}}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(tickets, hall_state):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "tickets": tickets,
            "hall_state": hall_state
        }, f, indent=2, ensure_ascii=False)
