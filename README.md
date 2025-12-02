# Windows System Optimizer

A comprehensive Windows optimization tool with a modern graphical user interface.

## Features

- **Network Optimizations**: TCP/IP settings, DNS cache, network adapter configurations
- **Graphics & GPU**: GPU driver settings, disable throttling, frame latency improvements
- **Power Management**: Maximum performance, CPU throttling disabled, power optimization
- **Privacy & Telemetry**: Disable telemetry, tracking, and data collection
- **System Services**: Disable unnecessary Windows services and scheduled tasks
- **Storage & File System**: Disk performance, indexing and compression optimization
- **Windows Updates**: Disable automatic updates and related services

## Quick Start

1. Install Python 3.7+ (with PATH option checked)
2. Open Command Prompt as Administrator
3. Run: `pip install -r requirements.txt`
4. Run: `python main.py` or double-click `run.bat`

## Requirements

- Windows 10/11
- Administrator privileges
- Python 3.7 or higher
- PyQt5

## Detailed Installation

See [INSTALLATION.md](INSTALLATION.md) for detailed installation instructions.

## Usage

See [USAGE.md](USAGE.md) for detailed usage instructions.

### Quick Overview

The GUI shows optimization categories as wide cards with toggle switches:
- **Red switch (left)**: Optimization is DISABLED
- **Green switch (right)**: Optimization is ENABLED

Click any switch to toggle that optimization on/off. No notifications will appear - only the switch color changes.

### Automatic Backup & Restore

- **Enabling**: Automatically backs up current settings, then applies optimization
- **Disabling**: Automatically restores from backup, then deletes backup file
- No manual intervention needed

### Apply All

Click the "✓ Apply All Optimizations" button at the top to enable all optimizations at once.

## GUI Preview

See [GUI_PREVIEW.md](GUI_PREVIEW.md) for a visual representation of the interface.

## Project Structure

```
factos/
├── main.py                  # Application entry point
├── run.bat                  # Windows batch file to launch
├── requirements.txt         # Python dependencies
├── optimizations/           # Optimization modules (7 categories)
│   ├── network.py          # Network & TCP/IP optimizations
│   ├── graphics.py         # Graphics/GPU optimizations
│   ├── power.py            # Power & performance settings
│   ├── privacy.py          # Privacy & telemetry controls
│   ├── services.py         # Windows services management
│   ├── storage.py          # Storage & file system optimization
│   └── updates.py          # Windows Update controls
├── backup_manager/          # Automatic backup system
│   └── manager.py          # Backup save/load/restore logic
├── gui/                     # Graphical user interface
│   └── main_window.py      # Main window with card-based design
└── backups/                 # Backup files (auto-generated)
```

## Safety & Reliability

- **Automatic Backups**: All changes are backed up before applying
- **Easy Reversion**: Toggle switch back to red to restore original settings
- **Independent Categories**: Each optimization category has its own backup
- **Persistent Backups**: Backups survive application restarts
- **Error Handling**: Graceful failure handling prevents system damage

## What This Tool Does

This optimizer applies proven Windows tweaks that:
- Reduce system latency
- Improve network performance
- Maximize CPU/GPU performance
- Disable telemetry and tracking
- Remove bloatware services
- Optimize disk I/O
- Give you control over updates

## What This Tool Does NOT Do

- Does not delete Windows files
- Does not install third-party software
- Does not modify user files
- Does not send data anywhere
- Does not require internet connection

## Compatibility

- Windows 10 (1909 and later)
- Windows 11 (all versions)
- 64-bit systems recommended
- May work on Windows Server (not officially tested)

## Contributing

This is a refactored and improved version of the original scripts. The new modular architecture makes it easy to:
- Add new optimization categories
- Modify existing optimizations
- Improve backup/restore logic
- Enhance the GUI

## License

Use at your own risk. Always create system restore points before running optimization tools.

## Credits

Refactored and modernized by GitHub Copilot from the original scripts.
