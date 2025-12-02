import subprocess
import winreg as reg

def apply():
    commands = [
        'fsutil behavior set memoryusage 2',
        'fsutil behavior set disablecompression 1',
        'fsutil behavior set disableencryption 1',
        'fsutil behavior set encryptpagingfile 0',
        'fsutil behavior set disable8dot3 1',
        'fsutil behavior set DisableDeleteNotify 0',
        'fsutil behavior set DisableLastAccess 1',
        'fsutil behavior set mftzone 4',
    ]
    
    for cmd in commands:
        try:
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
    
    registry_entries = [
        (r'SYSTEM\CurrentControlSet\Control\FileSystem', 'NtfsDisableLastAccessUpdate', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\FileSystem', 'NtfsMemoryUsage', 2, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\StorageSense', 'AllowStorageSenseGlobal', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters', 'EnablePrefetcher', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters', 'EnableSuperfetch', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\stornvme\Parameters\Device', 'DisableThrottling', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\stornvme\Parameters\Device', 'ThermalThrottling', 0, reg.REG_DWORD),
    ]
    
    for path, name, value, vtype in registry_entries:
        try:
            key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
            reg.SetValueEx(key, name, 0, vtype, value)
            reg.CloseKey(key)
        except:
            pass
    
    try:
        key = reg.CreateKeyEx(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy', 0, reg.KEY_WRITE)
        reg.SetValueEx(key, '01', 0, reg.REG_DWORD, 0)
        reg.CloseKey(key)
    except:
        pass

def get_backup_data():
    backup = {}
    backup['registry'] = []
    
    registry_paths = [
        (r'SYSTEM\CurrentControlSet\Control\FileSystem', ['NtfsDisableLastAccessUpdate', 'NtfsMemoryUsage']),
        (r'SOFTWARE\Policies\Microsoft\Windows\StorageSense', ['AllowStorageSenseGlobal']),
        (r'SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters', ['EnablePrefetcher', 'EnableSuperfetch']),
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
