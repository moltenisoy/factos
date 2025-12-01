import subprocess
import winreg
import os

devnull = subprocess.DEVNULL

media_output = subprocess.check_output('wmic diskdrive where (Index=0) get MediaType /format:list', shell=True).decode().strip()
media_lines = [line.strip() for line in media_output.split('\n') if line.strip()]
media = next((line.split('=')[1].strip() for line in media_lines if line.startswith('MediaType=')), '')

tipo_disco = 'DESCONOCIDO'
if media.startswith('Fixed'):
    tipo_disco = 'SSD'
elif media == 'Removable':
    tipo_disco = 'REMOVIBLE'
else:
    model_output = subprocess.check_output('wmic diskdrive where (Index=0) get Model /format:list', shell=True).decode().strip()
    model_lines = [line.strip() for line in model_output.split('\n') if line.strip()]
    model = next((line.split('=')[1].strip() for line in model_lines if line.startswith('Model=')), '')
    if model:
        tipo_disco = 'HDD'

subprocess.call(['fsutil', 'behavior', 'set', 'memoryusage', '2'], stdout=devnull, stderr=devnull)
subprocess.call(['fsutil', 'behavior', 'set', 'disablecompression', '1'], stdout=devnull, stderr=devnull)
subprocess.call(['fsutil', 'behavior', 'set', 'disableencryption', '1'], stdout=devnull, stderr=devnull)
subprocess.call(['fsutil', 'behavior', 'set', 'encryptpagingfile', '0'], stdout=devnull, stderr=devnull)
subprocess.call(['fsutil', 'behavior', 'set', 'disable8dot3', '1'], stdout=devnull, stderr=devnull)
subprocess.call(['fsutil', 'behavior', 'set', 'DisableDeleteNotify', '0'], stdout=devnull, stderr=devnull)
subprocess.call(['fsutil', 'behavior', 'set', 'DisableLastAccess', '1'], stdout=devnull, stderr=devnull)
subprocess.call(['fsutil', 'behavior', 'set', 'mftzone', '4'], stdout=devnull, stderr=devnull)
subprocess.call(['fsutil', 'usn', 'deletejournal', '/D', 'C:'], stdout=devnull, stderr=devnull)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\FileSystem', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'NtfsDisableLastAccessUpdate', 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(key, 'NtfsMemoryUsage', 0, winreg.REG_DWORD, 2)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\StorageSense', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'AllowStorageSenseGlobal', 0, winreg.REG_DWORD, 0)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, '01', 0, winreg.REG_DWORD, 0)
winreg.CloseKey(key)

subprocess.call(['schtasks', '/Change', '/TN', r'Microsoft\Windows\StorageSense\StorageSenseTask', '/Disable'], stdout=devnull, stderr=devnull)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'EnablePrefetcher', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'EnableSuperfetch', 0, winreg.REG_DWORD, 0)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\SysMain', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
winreg.CloseKey(key)

subprocess.call(['sc', 'config', 'SysMain', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'SysMain'], stdout=devnull, stderr=devnull)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management', 0, winreg.KEY_SET_VALUE)
if tipo_disco == 'SSD':
    winreg.SetValueEx(key, 'DisablePagingExecutive', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, 'LargeSystemCache', 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(key, 'IoPageLockLimit', 0, winreg.REG_DWORD, 0)
else:
    winreg.SetValueEx(key, 'DisablePagingExecutive', 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(key, 'LargeSystemCache', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, 'IoPageLockLimit', 0, winreg.REG_DWORD, 16777216)

winreg.SetValueEx(key, 'FeatureSettingsOverride', 0, winreg.REG_DWORD, 3)
winreg.SetValueEx(key, 'FeatureSettingsOverrideMask', 0, winreg.REG_DWORD, 3)
winreg.SetValueEx(key, 'FeatureSettings', 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(key, 'EnableCfg', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'MoveImages', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'ClearPageFileAtShutdown', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'SystemPages', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'PhysicalAddressExtension', 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(key, 'PoolUsageMaximum', 0, winreg.REG_DWORD, 96)
winreg.SetValueEx(key, 'PagedPoolSize', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'NonPagedPoolSize', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'SecondLevelDataCache', 0, winreg.REG_DWORD, 1024)
winreg.SetValueEx(key, 'SessionPoolSize', 0, winreg.REG_DWORD, 0)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'autodisconnect', 0, winreg.REG_DWORD, 4294967295)
winreg.SetValueEx(key, 'Size', 0, winreg.REG_DWORD, 3)
winreg.SetValueEx(key, 'IRPStackSize', 0, winreg.REG_DWORD, 50)
winreg.SetValueEx(key, 'SizReqBuf', 0, winreg.REG_DWORD, 170372)
winreg.SetValueEx(key, 'AutoShareWks', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'AutoShareServer', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'SMB1', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'RestrictNullSessAccess', 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

subprocess.call(['sc', 'config', 'defragsvc', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'config', 'vds', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'config', 'vss', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'config', 'swprv', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'config', 'vmicvss', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'defragsvc'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'vds'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'vss'], stdout=devnull, stderr=devnull)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows NT\DiskQuota', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'Enforce', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'Enable', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'LogEventOverLimit', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'LogEventOverThreshold', 0, winreg.REG_DWORD, 0)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\FileSystem', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'NtfsDisableLastAccessUpdate', 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(key, 'NtfsDisable8dot3NameCreation', 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

try:
    winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Classes\Microsoft.DiskQuota')
except:
    pass
try:
    winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Classes\Microsoft.DiskQuota.1')
except:
    pass

subprocess.call(['sc', 'config', 'wuauserv', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'wuauserv'], stdout=devnull, stderr=devnull)

subprocess.call(['sc', 'config', 'DoSvc', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'DoSvc'], stdout=devnull, stderr=devnull)

subprocess.call(['sc', 'config', 'UOSvc', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'UOSvc'], stdout=devnull, stderr=devnull)

subprocess.call(['sc', 'config', 'WaaSMedicSvc', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'WaaSMedicSvc'], stdout=devnull, stderr=devnull)

subprocess.call(['sc', 'config', 'bits', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'stop', 'bits'], stdout=devnull, stderr=devnull)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'DoNotConnectToWindowsUpdateInternetLocations', 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(key, 'SetDisableUXWUAccess', 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(key, 'ExcludeWUDriversInQualityUpdate', 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'NoAutoUpdate', 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(key, 'AUOptions', 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(key, 'NoAutoRebootWithLoggedOnUser', 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\WindowsUpdate\UX\Settings', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'PauseUpdatesExpiryTime', 0, winreg.REG_SZ, '2026-12-31T23:59:59Z')
winreg.SetValueEx(key, 'PauseFeatureUpdatesEndTime', 0, winreg.REG_SZ, '2026-12-31T23:59:59Z')
winreg.SetValueEx(key, 'PauseQualityUpdatesEndTime', 0, winreg.REG_SZ, '2026-12-31T23:59:59Z')
winreg.SetValueEx(key, 'PauseUpdatesStartTime', 0, winreg.REG_SZ, '2025-11-28T00:00:00Z')
winreg.SetValueEx(key, 'PauseFeatureUpdatesStartTime', 0, winreg.REG_SZ, '2025-11-28T00:00:00Z')
winreg.SetValueEx(key, 'PauseQualityUpdatesStartTime', 0, winreg.REG_SZ, '2025-11-28T00:00:00Z')
winreg.CloseKey(key)

hosts_path = os.path.join(os.environ['SystemRoot'], 'System32', 'drivers', 'etc', 'hosts')
with open(hosts_path, 'a') as f:
    f.write('\n0.0.0.0 windowsupdate.microsoft.com')
    f.write('\n0.0.0.0 *.update.microsoft.com')
    f.write('\n0.0.0.0 download.windowsupdate.com')
    f.write('\n0.0.0.0 windowsupdate.com')
    f.write('\n0.0.0.0 *.windowsupdate.com')
    f.write('\n0.0.0.0 *.delivery.mp.microsoft.com')
    f.write('\n0.0.0.0 storeedgefd.microsoft.com')
    f.write('\n0.0.0.0 *.msftconnecttest.com')

subprocess.call(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=Bloquear Windows Update', 'dir=out', 'action=block', 'remoteip=20.190.0.0/13,40.64.0.0/10,13.64.0.0/10,52.160.0.0/11', 'enable=yes'], stdout=devnull, stderr=devnull)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\WindowsStore', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'AutoDownload', 0, winreg.REG_DWORD, 2)
winreg.SetValueEx(key, 'RemoveWindowsStore', 0, winreg.REG_DWORD, 0)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows Defender\Signature Updates', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'UpdateOnStartup', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'ASSignatureDue', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'AVSignatureDue', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'ForceUpdateFromMU', 0, winreg.REG_DWORD, 0)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows Defender', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'DisableAntiSpyware', 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

subprocess.call(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\WindowsUpdate\Scheduled Start', '/Disable'], stdout=devnull, stderr=devnull)
subprocess.call(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\WindowsUpdate\Automatic App Update', '/Disable'], stdout=devnull, stderr=devnull)
subprocess.call(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\UpdateOrchestrator\Schedule Scan', '/Disable'], stdout=devnull, stderr=devnull)
subprocess.call(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\UpdateOrchestrator\Universal Orchestrator Start', '/Disable'], stdout=devnull, stderr=devnull)

subprocess.call(['powercfg', '-h', 'off'], stdout=devnull, stderr=devnull)
subprocess.call(['wuauclt', '/resetauthorization', '/detectnow'], stdout=devnull, stderr=devnull)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\XboxNetApiSvc', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\XboxGipSvc', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\XblAuthManager', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
winreg.CloseKey(key)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\XblGameSave', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
winreg.CloseKey(key)

subprocess.call(['schtasks', '/end', '/tn', r'\Microsoft\XblGameSave\XblGameSaveTask'], stdout=devnull, stderr=devnull)
subprocess.call(['schtasks', '/change', '/tn', r'\Microsoft\XblGameSave\XblGameSaveTask', '/disable'], stdout=devnull, stderr=devnull)
subprocess.call(['schtasks', '/end', '/tn', r'\Microsoft\XblGameSave\XblGameSaveTaskLogon'], stdout=devnull, stderr=devnull)
subprocess.call(['schtasks', '/change', '/tn', r'\Microsoft\XblGameSave\XblGameSaveTaskLogon', '/disable'], stdout=devnull, stderr=devnull)

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\GameBar', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'AutoGameModeEnabled', 0, winreg.REG_DWORD, 0)
winreg.SetValueEx(key, 'AllowAutoGameMode', 0, winreg.REG_DWORD, 0)
winreg.CloseKey(key)

subprocess.call(['sc', 'config', 'xbgm', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'config', 'XblAuthManager', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'config', 'XblGameSave', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'config', 'XboxGipSvc', 'start=', 'disabled'], stdout=devnull, stderr=devnull)
subprocess.call(['sc', 'config', 'XboxNetApiSvc', 'start=', 'disabled'], stdout=devnull, stderr=devnull)