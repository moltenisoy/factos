import json
import subprocess
import os
from pathlib import Path
from datetime import datetime


def run_command(cmd, capture_output=True):
    """Execute a command and optionally capture output"""
    try:
        if capture_output:
            result = subprocess.run(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                text=True
            )
            return result.stdout
        else:
            subprocess.run(
                cmd,
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False
            )
            return None
    except Exception as e:
        return None


def export_registry_key(key_path, output_file):
    """Export a registry key to a .reg file"""
    try:
        cmd = f'reg export "{key_path}" "{output_file}" /y'
        run_command(cmd, capture_output=False)
        return Path(output_file).exists()
    except Exception:
        return False


def import_registry_file(reg_file):
    """Import a .reg file to restore registry settings"""
    try:
        if not Path(reg_file).exists():
            return False
        cmd = f'reg import "{reg_file}"'
        run_command(cmd, capture_output=False)
        return True
    except Exception:
        return False


def backup_registry_keys(category_name, backup_dir):
    """Backup relevant registry keys for a category"""
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # Define registry keys to backup per category
    registry_keys = {
        'network': [
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip',
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip6',
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\AFD',
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Dnscache',
            r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched',
            r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient',
        ],
        'privacy': [
            r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection',
            r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection',
            r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo',
            r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\AdvertisingInfo',
            r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
            r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent',
            r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\SQMClient',
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DiagTrack',
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\dmwappushservice',
        ],
        'services': [
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services',
        ],
        'graphics': [
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}',
            r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile',
        ],
        'power': [
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power',
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power',
        ],
        'storage': [
            r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\stornvme',
        ],
        'full': []  # Will backup all above
    }
    
    # Get keys for this category
    keys_to_backup = registry_keys.get(category_name, [])
    if category_name == 'full':
        # Backup all keys for full optimization
        keys_to_backup = []
        for cat_keys in registry_keys.values():
            keys_to_backup.extend(cat_keys)
    
    # Export each registry key
    backed_up_keys = []
    for i, key_path in enumerate(keys_to_backup):
        output_file = backup_dir / f"{category_name}_reg_{i:03d}.reg"
        if export_registry_key(key_path, str(output_file)):
            backed_up_keys.append({
                'key': key_path,
                'file': str(output_file)
            })
    
    return backed_up_keys


def backup_services_state(backup_dir):
    """Backup current state of Windows services"""
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    services_file = backup_dir / "services_state.txt"
    
    try:
        # Get all services and their startup type
        cmd = 'sc query type= service state= all'
        output = run_command(cmd, capture_output=True)
        
        if output:
            with open(services_file, 'w', encoding='utf-8') as f:
                f.write(output)
            return str(services_file)
    except Exception:
        pass
    
    return None


def backup_netsh_settings(backup_dir):
    """Backup netsh network settings"""
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    netsh_file = backup_dir / "netsh_settings.txt"
    
    try:
        # Backup various netsh settings
        commands = [
            'netsh int tcp show global',
            'netsh int ipv4 show global',
            'netsh int ipv6 show global',
            'netsh interface show interface',
            'netsh advfirewall show allprofiles',
        ]
        
        with open(netsh_file, 'w', encoding='utf-8') as f:
            for cmd in commands:
                f.write(f"\n{'='*60}\n")
                f.write(f"Command: {cmd}\n")
                f.write(f"{'='*60}\n\n")
                output = run_command(cmd, capture_output=True)
                if output:
                    f.write(output)
                f.write("\n")
        
        return str(netsh_file)
    except Exception:
        pass
    
    return None


def backup_power_settings(backup_dir):
    """Backup power plan settings"""
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    power_file = backup_dir / "power_settings.txt"
    
    try:
        # Get current power plan
        cmd = 'powercfg /list'
        output = run_command(cmd, capture_output=True)
        
        if output:
            with open(power_file, 'w', encoding='utf-8') as f:
                f.write(output)
            return str(power_file)
    except Exception:
        pass
    
    return None


def create_full_backup(category_name):
    """Create a comprehensive backup before applying optimizations"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(f"backup_{category_name}_{timestamp}")
    
    backup_info = {
        'category': category_name,
        'timestamp': timestamp,
        'backup_directory': str(backup_dir),
        'registry_backups': [],
        'services_backup': None,
        'netsh_backup': None,
        'power_backup': None,
    }
    
    try:
        # Create backup directory
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Backup registry keys
        registry_backups = backup_registry_keys(category_name, backup_dir)
        backup_info['registry_backups'] = registry_backups
        
        # Backup services state
        services_backup = backup_services_state(backup_dir)
        if services_backup:
            backup_info['services_backup'] = services_backup
        
        # Backup netsh settings (for network category)
        if category_name in ['network', 'full']:
            netsh_backup = backup_netsh_settings(backup_dir)
            if netsh_backup:
                backup_info['netsh_backup'] = netsh_backup
        
        # Backup power settings (for power category)
        if category_name in ['power', 'full']:
            power_backup = backup_power_settings(backup_dir)
            if power_backup:
                backup_info['power_backup'] = power_backup
        
        # Save backup metadata
        metadata_file = backup_dir / "backup_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(backup_info, f, indent=2)
        
        return backup_info
        
    except Exception as e:
        return None


def restore_from_backup(backup_info):
    """Restore system settings from backup"""
    if not backup_info:
        return False
    
    try:
        # Restore registry keys
        for reg_backup in backup_info.get('registry_backups', []):
            reg_file = reg_backup.get('file')
            if reg_file and Path(reg_file).exists():
                import_registry_file(reg_file)
        
        # Note: Services and netsh settings require manual restoration
        # as they can't be automatically restored without risk
        
        return True
    except Exception:
        return False


def save_backup(filename, backup_data):
    """Legacy function for compatibility - saves backup metadata"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, indent=2)
        return True
    except Exception:
        return False


def load_backup(filename):
    """Legacy function for compatibility - loads backup metadata"""
    try:
        if not Path(filename).exists():
            return None
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


def has_backup(filename):
    """Check if backup file exists"""
    return Path(filename).exists()


def delete_backup(filename):
    """Delete backup file"""
    try:
        if Path(filename).exists():
            Path(filename).unlink()
        return True
    except Exception:
        return False
