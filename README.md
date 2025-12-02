# Windows System Optimizer

A comprehensive Windows optimization tool with a graphical user interface.

## Features

- **Network Optimizations**: TCP/IP settings, DNS cache, network adapter configurations
- **Graphics & GPU**: GPU driver settings, disable throttling, frame latency improvements
- **Power Management**: Maximum performance, CPU throttling disabled, power optimization
- **Privacy & Telemetry**: Disable telemetry, tracking, and data collection
- **System Services**: Disable unnecessary Windows services and scheduled tasks
- **Storage & File System**: Disk performance, indexing and compression optimization
- **Windows Updates**: Disable automatic updates and related services

## Requirements

- Windows 10/11
- Administrator privileges
- Python 3.7+
- PyQt5

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the application as administrator:

```bash
python main.py
```

The GUI will show optimization categories as cards with toggle switches:
- **Red switch**: Optimization is disabled
- **Green switch**: Optimization is enabled

### Automatic Backup

When you enable an optimization, a backup is automatically created. When you disable it, the backup is restored.

### Apply All

Use the "Apply All Optimizations" button at the top to enable all optimizations at once.

## Structure

```
factos/
├── main.py                  # Entry point
├── optimizations/           # Optimization modules
│   ├── network.py          # Network optimizations
│   ├── graphics.py         # Graphics/GPU optimizations
│   ├── power.py            # Power management
│   ├── privacy.py          # Privacy and telemetry
│   ├── services.py         # System services
│   ├── storage.py          # Storage optimizations
│   └── updates.py          # Windows Update control
├── backup_manager/          # Backup system
│   └── manager.py
└── gui/                     # GUI interface
    └── main_window.py
```

## Safety

All modifications are backed up automatically before being applied. You can safely revert any changes by toggling the switch back to red.
