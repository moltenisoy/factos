# Usage Guide

## Understanding the Interface

The Windows Optimizer uses a card-based interface where each card represents a category of optimizations.

### Toggle Switches

Each optimization card has a toggle switch on the right:

- **Red (Left Position)**: Optimization is DISABLED
- **Green (Right Position)**: Optimization is ENABLED

Click the switch to toggle between states.

## Optimization Categories

### 1. Network Optimizations
Optimizes TCP/IP parameters, DNS cache settings, network adapter configurations, and service priorities. Improves network performance and reduces latency.

### 2. Graphics & GPU
Disables GPU power throttling, optimizes driver settings, reduces frame latency, and improves graphics performance for gaming and professional applications.

### 3. Power Management
Maximizes CPU performance, disables power throttling, optimizes boot configuration, and sets all power profiles to high performance mode.

### 4. Privacy & Telemetry
Disables Windows telemetry services, tracking, diagnostic data collection, and advertising features. Improves privacy and reduces background activity.

### 5. System Services
Disables unnecessary Windows services and scheduled tasks that consume system resources without providing benefit to most users.

### 6. Storage & File System
Optimizes file system performance, disables indexing and compression, improves disk I/O, and disables storage sense features.

### 7. Windows Updates
Disables automatic Windows updates and related services. Gives you full control over when to update your system.

## How to Use

### Enable Single Optimization

1. Click the red toggle switch on the desired optimization card
2. The switch will turn green
3. A backup is automatically created
4. The optimization is applied immediately
5. No notification will appear - the switch color change confirms success

### Disable Single Optimization

1. Click the green toggle switch on the enabled optimization
2. The switch will turn red
3. The backup is automatically restored
4. Changes are reverted immediately
5. No notification will appear - the switch color change confirms success

### Enable All Optimizations

1. Click the "✓ Apply All Optimizations" button at the top
2. All optimizations will be enabled
3. Backups are created for all modifications
4. All switches will turn green
5. This happens silently in the background

## Backup System

### Automatic Backups

- Backups are created automatically when you enable an optimization
- Stored in the `backups/` folder as JSON files
- One backup file per optimization category
- Contains all registry values and service states before modification

### Automatic Restore

- When you disable an optimization, the backup is automatically loaded
- All changes are reverted to their original state
- The backup file is then deleted
- No manual intervention required

### Safety Features

- Cannot accidentally lose your original settings
- Each category has independent backup
- Backups persist between application restarts
- If you close the app with optimizations enabled, they remain enabled
- Backups are preserved until you manually disable the optimization

## Important Notes

### Administrator Privileges

The application MUST run with administrator privileges to:
- Modify system registry settings
- Configure Windows services
- Change boot configuration
- Apply network settings

The application will automatically request elevation when launched.

### System Restart

Some optimizations may require a system restart to fully take effect:
- Boot configuration changes
- Some driver settings
- Certain power management features

However, most changes take effect immediately.

### Reversion

To revert all changes:
1. Toggle all green switches to red
2. Or reinstall Windows (not recommended, use the toggles instead!)

### Compatibility

- Tested on Windows 10 (1909 and later)
- Compatible with Windows 11
- May work on Windows Server editions (not officially supported)

## Tips

- Enable optimizations one at a time to see individual effects
- Some optimizations are more impactful than others
- Network and Power optimizations usually show immediate results
- Privacy optimizations reduce background activity
- Storage optimizations improve disk performance over time

## What NOT to Do

- Don't manually delete backup files while optimizations are enabled
- Don't modify registry keys that were changed by optimizations
- Don't disable services manually that were optimized by the tool
- Don't run multiple optimization tools simultaneously

## Getting Help

If an optimization causes issues:
1. Simply toggle the switch back to red
2. The original state will be restored
3. Restart your computer if needed
4. The issue should be resolved

If you cannot access the GUI:
1. Boot into Safe Mode
2. Delete the corresponding backup file in `backups/` folder
3. Restart normally
