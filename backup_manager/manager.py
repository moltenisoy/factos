import json
import os
from pathlib import Path

BACKUP_DIR = Path(__file__).parent.parent / 'backups'

def ensure_backup_dir():
    BACKUP_DIR.mkdir(exist_ok=True)

def save_backup(category_name, backup_data):
    ensure_backup_dir()
    backup_file = BACKUP_DIR / f'{category_name}.json'
    with open(backup_file, 'w') as f:
        json.dump(backup_data, f, indent=2)

def load_backup(category_name):
    backup_file = BACKUP_DIR / f'{category_name}.json'
    if not backup_file.exists():
        return None
    with open(backup_file, 'r') as f:
        return json.load(f)

def has_backup(category_name):
    backup_file = BACKUP_DIR / f'{category_name}.json'
    return backup_file.exists()

def delete_backup(category_name):
    backup_file = BACKUP_DIR / f'{category_name}.json'
    if backup_file.exists():
        backup_file.unlink()
