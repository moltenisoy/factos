import subprocess
import winreg as reg

def apply():
    commands = [
        'bcdedit /set disabledynamictick yes',
        'bcdedit /deletevalue useplatformclock',
        'bcdedit /set useplatformtick yes',
        'bcdedit /set tscsyncpolicy Enhanced',
        'bcdedit /set MSI default',
        'bcdedit /set usephysicaldestination no',
        'bcdedit /set usefirmwarepcisettings no',
        'bcdedit /set x2apicpolicy enable',
        'bcdedit /set tpmbootentropy ForceDisable',
        'powercfg /setacvalueindex scheme_current sub_processor CPMINCORES 100',
        'powercfg /setdcvalueindex scheme_current sub_processor CPMINCORES 100',
        'powercfg /setacvalueindex scheme_current sub_processor PROCTHROTTLING 0',
        'powercfg /setdcvalueindex scheme_current sub_processor PROCTHROTTLING 0',
        'powercfg -setacvalueindex scheme_current sub_disk 0b2d69d7-a2a1-449c-9680-f91c70521c60 0',
        'powercfg -setdcvalueindex scheme_current sub_disk 0b2d69d7-a2a1-449c-9680-f91c70521c60 0',
        'powercfg -setacvalueindex scheme_current sub_pciExpress ee12f906-d277-404b-b6da-e5fa1a576df5 0',
        'powercfg -setdcvalueindex scheme_current sub_pciExpress ee12f906-d277-404b-b6da-e5fa1a576df5 0',
        'powercfg /setactive scheme_current',
        'powercfg -h off',
    ]
    
    for cmd in commands:
        try:
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
    
    registry_entries = [
        (r'SYSTEM\CurrentControlSet\Control\Power', 'ExitLatency', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Power', 'ExitLatencyCheckEnabled', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Power', 'HighPerformance', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Power', 'InitialUnparkCount', 100, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Power\PowerThrottling', 'PowerThrottlingOff', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Power', 'EnergyEstimationEnabled', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Power', 'MinimumThrottlePercent', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Power', 'MaximumThrottlePercent', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Power', 'PowerThrottlingOff', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Session Manager\Power', 'HiberbootEnabled', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\PriorityControl', 'Win32PrioritySeparation', 38, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile', 'NetworkThrottlingIndex', 4294967295, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile', 'SystemResponsiveness', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile', 'AlwaysOn', 1, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile', 'NoLazyMode', 1, reg.REG_DWORD),
    ]
    
    for path, name, value, vtype in registry_entries:
        try:
            key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
            reg.SetValueEx(key, name, 0, vtype, value)
            reg.CloseKey(key)
        except:
            pass

def get_backup_data():
    backup = {}
    backup['registry'] = []
    
    registry_paths = [
        (r'SYSTEM\CurrentControlSet\Control\Power', ['ExitLatency', 'HighPerformance', 'EnergyEstimationEnabled', 'PowerThrottlingOff']),
        (r'SYSTEM\CurrentControlSet\Control\PriorityControl', ['Win32PrioritySeparation']),
        (r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile', ['SystemResponsiveness', 'NetworkThrottlingIndex']),
    ]
    
    for path, value_names in registry_paths:
        try:
            key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_READ)
            for name in value_names:
                try:
                    value, vtype = reg.QueryValueEx(key, name)
                    backup['registry'].append((path, name, value, vtype))
                except:
                    backup['registry'].append((path, name, None, None))
            reg.CloseKey(key)
        except:
            pass
    
    return backup

def restore(backup_data):
    if not backup_data:
        return
    
    for path, name, value, vtype in backup_data.get('registry', []):
        try:
            if value is not None:
                key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
                reg.SetValueEx(key, name, 0, vtype, value)
                reg.CloseKey(key)
        except:
            pass
