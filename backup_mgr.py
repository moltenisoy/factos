import json
from pathlib import Path

def save_backup(filename, backup_data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, indent=2)
        return True
    except Exception:
        return False

def load_backup(filename):
    try:
        if not Path(filename).exists():
            return None
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None

def has_backup(filename):
    return Path(filename).exists()

def delete_backup(filename):
    try:
        if Path(filename).exists():
            Path(filename).unlink()
        return True
    except Exception:
        return False
