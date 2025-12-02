import subprocess
import os
import json
import re
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
                text=True,
                encoding='utf-8',
                errors='ignore'
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
    except Exception:
        return None


def parse_registry_command(cmd):
    """Parse a registry command to extract key, value name, type, and data"""
    if 'reg' not in cmd.lower() or 'add' not in cmd.lower():
        return None
    
    result = {}
    
    # Remove escaped quotes and backslashes for parsing
    clean_cmd = cmd.replace('\\"', '"').replace('\\\\', '\\')
    
    # Extract registry key path (between first quotes after "add")
    key_match = re.search(r'add\s+"([^"]+)"', clean_cmd, re.IGNORECASE)
    if key_match:
        result['key'] = key_match.group(1)
    
    # Extract value name (/v or /V)
    value_match = re.search(r'/v\s+"([^"]+)"|/v\s+(\S+)', clean_cmd, re.IGNORECASE)
    if value_match:
        result['value_name'] = value_match.group(1) or value_match.group(2)
    
    # Extract type (/t)
    type_match = re.search(r'/t\s+(\S+)', clean_cmd, re.IGNORECASE)
    if type_match:
        result['type'] = type_match.group(1)
    
    # Extract data (/d)
    data_match = re.search(r'/d\s+"([^"]+)"|/d\s+(\S+)', clean_cmd, re.IGNORECASE)
    if data_match:
        result['data'] = data_match.group(1) or data_match.group(2)
    
    return result if 'key' in result else None


def read_registry_value(key_path, value_name):
    """Read current value from registry"""
    try:
        cmd = f'reg query "{key_path}" /v "{value_name}"'
        output = run_command(cmd, capture_output=True)
        
        if output and 'ERROR' not in output:
            # Parse output to get current value
            # Format: "    ValueName    REG_TYPE    Value"
            lines = output.strip().split('\n')
            for line in lines:
                if value_name.lower() in line.lower():
                    parts = line.split()
                    if len(parts) >= 3:
                        return {
                            'type': parts[-2] if 'REG_' in parts[-2] else parts[1],
                            'data': parts[-1] if 'REG_' in parts[-2] else ' '.join(parts[2:])
                        }
        return None
    except Exception:
        return None


def parse_service_command(cmd):
    """Parse a service configuration command"""
    if 'sc config' not in cmd.lower() and 'sc stop' not in cmd.lower() and 'sc start' not in cmd.lower():
        return None
    
    result = {}
    
    # Extract service name
    if 'sc config' in cmd.lower():
        match = re.search(r'sc\s+config\s+"?([^"\s]+)"?\s+start', cmd, re.IGNORECASE)
        if match:
            result['service'] = match.group(1).strip('"')
            result['action'] = 'config'
            
            # Extract startup type
            start_match = re.search(r'start\s*=?\s*(\w+)', cmd, re.IGNORECASE)
            if start_match:
                result['start_type'] = start_match.group(1)
    
    elif 'sc stop' in cmd.lower() or 'sc start' in cmd.lower():
        match = re.search(r'sc\s+(stop|start)\s+"?([^"\s]+)"?', cmd, re.IGNORECASE)
        if match:
            result['action'] = match.group(1)
            result['service'] = match.group(2).strip('"')
    
    return result if 'service' in result else None


def read_service_state(service_name):
    """Read current service configuration"""
    try:
        cmd = f'sc qc "{service_name}"'
        output = run_command(cmd, capture_output=True)
        
        if output and 'FAILED' not in output:
            state = {}
            
            # Extract START_TYPE
            start_match = re.search(r'START_TYPE\s+:\s+\d+\s+(\w+)', output, re.IGNORECASE)
            if start_match:
                state['start_type'] = start_match.group(1)
            
            # Extract current state
            cmd_status = f'sc query "{service_name}"'
            status_output = run_command(cmd_status, capture_output=True)
            if status_output:
                state_match = re.search(r'STATE\s+:\s+\d+\s+(\w+)', status_output, re.IGNORECASE)
                if state_match:
                    state['current_state'] = state_match.group(1)
            
            return state if state else None
        return None
    except Exception:
        return None


def parse_netsh_command(cmd):
    """Parse a netsh command"""
    if not cmd.lower().startswith('netsh '):
        return None
    
    return {
        'type': 'netsh',
        'command': cmd
    }


def read_netsh_state(cmd_type):
    """Read current netsh state"""
    try:
        # Determine which netsh command to query
        if 'tcp' in cmd_type.lower():
            cmd = 'netsh int tcp show global'
        elif 'ipv4' in cmd_type.lower():
            cmd = 'netsh int ipv4 show global'
        elif 'ipv6' in cmd_type.lower():
            cmd = 'netsh int ipv6 show global'
        elif 'interface' in cmd_type.lower():
            cmd = 'netsh interface show interface'
        else:
            cmd = 'netsh int tcp show global'
        
        output = run_command(cmd, capture_output=True)
        return output if output else None
    except Exception:
        return None


def create_comprehensive_backup(category_name, commands):
    """Create a comprehensive backup for ALL commands in a category"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(f"backup_{category_name}_{timestamp}")
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    backup_data = {
        'category': category_name,
        'timestamp': timestamp,
        'backup_directory': str(backup_dir),
        'registry_values': [],
        'service_states': [],
        'netsh_states': [],
        'parsed_commands': 0,
        'backed_up_items': 0
    }
    
    # Create a .reg file for registry backups
    reg_file_path = backup_dir / f"{category_name}_registry_backup.reg"
    reg_file_lines = [
        'Windows Registry Editor Version 5.00',
        '',
        f'; Backup created: {timestamp}',
        f'; Category: {category_name}',
        ''
    ]
    
    # Parse and backup each command
    for cmd in commands:
        backup_data['parsed_commands'] += 1
        
        # Handle registry commands
        reg_info = parse_registry_command(cmd)
        if reg_info:
            current_value = read_registry_value(reg_info['key'], reg_info['value_name'])
            if current_value:
                backup_data['registry_values'].append({
                    'key': reg_info['key'],
                    'value_name': reg_info['value_name'],
                    'current_type': current_value.get('type'),
                    'current_data': current_value.get('data'),
                    'new_type': reg_info.get('type'),
                    'new_data': reg_info.get('data')
                })
                
                # Add to .reg file in proper Windows format
                reg_file_lines.append(f'[{reg_info["key"]}]')
                value_type = current_value.get('type', 'REG_SZ')
                data_value = current_value.get('data', '')
                
                # Format based on type
                if 'DWORD' in value_type.upper():
                    # DWORD format: dword:00000001
                    try:
                        dword_val = int(data_value, 16) if isinstance(data_value, str) and data_value.startswith('0x') else int(data_value)
                        reg_file_lines.append(f'"{reg_info["value_name"]}"=dword:{dword_val:08x}')
                    except:
                        reg_file_lines.append(f'"{reg_info["value_name"]}"=dword:00000000')
                else:
                    # String format: "value"
                    reg_file_lines.append(f'"{reg_info["value_name"]}"="{data_value}"')
                
                reg_file_lines.append('')
                
                backup_data['backed_up_items'] += 1
        
        # Handle service commands
        svc_info = parse_service_command(cmd)
        if svc_info:
            current_state = read_service_state(svc_info['service'])
            if current_state:
                backup_data['service_states'].append({
                    'service': svc_info['service'],
                    'action': svc_info.get('action'),
                    'current_start_type': current_state.get('start_type'),
                    'current_state': current_state.get('current_state'),
                    'new_start_type': svc_info.get('start_type')
                })
                backup_data['backed_up_items'] += 1
        
        # Handle netsh commands
        netsh_info = parse_netsh_command(cmd)
        if netsh_info:
            current_state = read_netsh_state(cmd)
            if current_state:
                backup_data['netsh_states'].append({
                    'command': cmd,
                    'current_state': current_state
                })
                backup_data['backed_up_items'] += 1
    
    # Save .reg file with UTF-16 LE encoding (Windows standard)
    with open(reg_file_path, 'w', encoding='utf-16') as f:
        # utf-16 encoding includes BOM automatically
        f.write('\r\n'.join(reg_file_lines))
    
    # Save JSON metadata
    metadata_file = backup_dir / "backup_metadata.json"
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(backup_data, f, indent=2)
    
    # Save service restoration script
    if backup_data['service_states']:
        service_restore = backup_dir / "restore_services.bat"
        with open(service_restore, 'w', encoding='utf-8') as f:
            f.write('@echo off\n')
            f.write(f'REM Service restoration script for {category_name}\n')
            f.write(f'REM Created: {timestamp}\n\n')
            for svc in backup_data['service_states']:
                if svc.get('current_start_type'):
                    f.write(f'sc config "{svc["service"]}" start= {svc["current_start_type"]}\n')
    
    # Save netsh restoration script
    if backup_data['netsh_states']:
        netsh_restore = backup_dir / "netsh_state.txt"
        with open(netsh_restore, 'w', encoding='utf-8') as f:
            f.write(f'Netsh State Backup for {category_name}\n')
            f.write(f'Created: {timestamp}\n\n')
            for i, state in enumerate(backup_data['netsh_states'], 1):
                f.write(f'\n{"="*60}\n')
                f.write(f'Command {i}: {state["command"]}\n')
                f.write(f'{"="*60}\n')
                f.write(state.get('current_state', 'No state captured') + '\n')
    
    return backup_data


def restore_from_comprehensive_backup(backup_dir):
    """Restore from a comprehensive backup"""
    backup_dir = Path(backup_dir)
    if not backup_dir.exists():
        return False
    
    try:
        # Restore registry from .reg file
        reg_files = list(backup_dir.glob("*_registry_backup.reg"))
        for reg_file in reg_files:
            cmd = f'reg import "{reg_file}"'
            run_command(cmd, capture_output=False)
        
        # Restore services
        service_scripts = list(backup_dir.glob("restore_services.bat"))
        for script in service_scripts:
            run_command(str(script), capture_output=False)
        
        return True
    except Exception:
        return False
