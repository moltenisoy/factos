# Windows System Optimizer - Complete Edition

A comprehensive Windows optimization tool with ALL optimizations from the original scripts included.

## Features

- **ALL Original Optimizations Included**: 2764+ commands from windows_optimizer.py
- **Flat Directory Structure**: All files in one folder for simplicity
- **Automatic Backup**: Backups stored in the same directory
- **Modern GUI**: Card-based interface with toggle switches
- **Silent Operation**: No notifications, only visual feedback

## Quick Start

1. Install Python 3.7+ (with PATH option checked)
2. Open Command Prompt as Administrator
3. Run: `pip install -r requirements.txt`
4. Run: `python app_gui.py` or double-click `run.bat`

## Requirements

- Windows 10/11
- Administrator privileges
- Python 3.7 or higher
- PyQt5

## File Structure (Flat - Single Directory)

```
factos/
├── app_gui.py              # Main GUI application
├── main.py                 # Alternative entry point
├── backup_mgr.py           # Backup system
├── opt_full.py             # ALL optimizations (2764 commands)
├── opt_graphics.py         # Graphics optimizations
├── backup_*.json           # Backup files (auto-created)
├── run.bat                 # Windows launcher
└── requirements.txt        # Dependencies
```

## Usage

### GUI Interface

The GUI shows optimization cards with toggle switches:
- **Red switch (left)**: Optimization is DISABLED
- **Green switch (right)**: Optimization is ENABLED

Click any switch to toggle that optimization on/off.

### Automatic Backup

- **Enabling**: Creates backup file (backup_*.json), then applies all optimizations
- **Disabling**: Deletes backup file (restoration happens automatically)
- Backup files are stored in the same directory as the application

### Apply All

Click the "✓ Apply All Optimizations" button to enable all optimizations at once.

## What's Included

### opt_full.py (2764 Commands)
ALL optimizations from the original windows_optimizer.py:
- Network: TCP/IP, DNS, firewall settings
- Graphics: GPU drivers, DWM, display settings
- Power: CPU, boot configuration, power plans
- Privacy: Telemetry, diagnostics, tracking
- Services: Windows services, scheduled tasks
- Storage: File system, indexing, compression
- Updates: Windows Update control
- And hundreds more...

## Safety

- **Backup Before Apply**: System state is backed up before modifications
- **Easy Revert**: Toggle switch back to restore original settings
- **Error Handling**: Graceful failure prevents system damage
- **No Deletion**: Original files preserved for reference

## Compatibility

- Windows 10 (1909+)
- Windows 11 (all versions)
- Requires Administrator privileges

## Notes

- All files are in a single directory as requested
- Backup files (backup_*.json) are in the same directory
- NO subdirectories - completely flat structure
- ALL optimizations from original files included
