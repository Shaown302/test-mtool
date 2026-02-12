import json
import os

DATA_FILES = {
    "users": "data/users.json",
    "stats": "data/stats.json",
    "gban": "data/gban.json",
    "models": "data/models.json",
    "memory": "data/memory.json"
}

def load_data(name):
    path = DATA_FILES[name]
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({}, f)
    with open(path, "r") as f:
        return json.load(f)

def save_data(name, data):
    with open(DATA_FILES[name], "w") as f:
        json.dump(data, f, indent=4)
