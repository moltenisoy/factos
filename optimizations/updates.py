import subprocess
import winreg as reg

def apply():
    services = [
        ('wuauserv', 'disabled'),
        ('DoSvc', 'disabled'),
        ('UsoSvc', 'disabled'),
        ('WaaSMedicSvc', 'disabled'),
        ('BITS', 'disabled'),
    ]
    
    for service, start_type in services:
        try:
            subprocess.run(f'sc config "{service}" start={start_type}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(f'sc stop "{service}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
    
    registry_entries = [
        (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'DoNotConnectToWindowsUpdateInternetLocations', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'SetDisableUXWUAccess', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 'ExcludeWUDriversInQualityUpdate', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', 'NoAutoUpdate', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', 'AUOptions', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', 'NoAutoRebootWithLoggedOnUser', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows Defender\Signature Updates', 'UpdateOnStartup', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows Defender', 'DisableAntiSpyware', 1, reg.REG_DWORD),
    ]
    
    for path, name, value, vtype in registry_entries:
        try:
            key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
            reg.SetValueEx(key, name, 0, vtype, value)
            reg.CloseKey(key)
        except:
            pass
    
    tasks = [
        r'Microsoft\Windows\WindowsUpdate\Scheduled Start',
        r'Microsoft\Windows\WindowsUpdate\Automatic App Update',
        r'Microsoft\Windows\UpdateOrchestrator\Schedule Scan',
        r'Microsoft\Windows\InstallService\ScanForUpdates',
        r'Microsoft\Windows\InstallService\ScanForUpdatesAsUser',
        r'Microsoft\Windows\WaaSMedic\PerformRemediation',
    ]
    
    for task in tasks:
        try:
            subprocess.run(f'schtasks /Change /TN "{task}" /Disable', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

def get_backup_data():
    backup = {}
    backup['services'] = []
    backup['registry'] = []
    return backup

def restore(backup_data):
    if not backup_data:
        return
