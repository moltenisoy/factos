import subprocess
import winreg as reg

def apply():
    services = [
        ('DiagTrack', 'disabled'),
        ('dmwappushservice', 'disabled'),
        ('diagnosticshub.standardcollector.service', 'disabled'),
    ]
    
    for service, start_type in services:
        try:
            subprocess.run(f'sc config "{service}" start={start_type}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(f'sc stop "{service}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
    
    registry_entries = [
        (r'SOFTWARE\Policies\Microsoft\Windows\DataCollection', 'AllowTelemetry', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\DataCollection', 'DoNotShowFeedbackNotifications', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\CloudContent', 'DisableThirdPartySuggestions', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\CloudContent', 'DisableWindowsConsumerFeatures', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\CloudContent', 'DisableSoftLanding', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\AdvertisingInfo', 'DisabledByGroupPolicy', 1, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo', 'Enabled', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\AppCompat', 'DisableInventory', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\AppCompat', 'AITEnable', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\AppCompat', 'DisableUAR', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\System', 'PublishUserActivities', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\System', 'EnableActivityFeed', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\SQMClient\Windows', 'CEIPEnable', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\SQMClient\Reliability', 'CEIPEnable', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\SQMClient\Reliability', 'SqmLoggerRunning', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\HandwritingErrorReports', 'PreventHandwritingErrorReports', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors', 'DisableLocation', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors', 'DisableSensors', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Biometrics', 'Enabled', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection', 'AllowTelemetry', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\SettingSync', 'DisableSettingSync', 2, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\WindowsAI', 'DisableAIDataAnalysis', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\OneDrive', 'DisableFileSyncNGSC', 1, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\System', 'AllowClipboardHistory', 0, reg.REG_DWORD),
    ]
    
    for path, name, value, vtype in registry_entries:
        try:
            key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
            reg.SetValueEx(key, name, 0, vtype, value)
            reg.CloseKey(key)
        except:
            pass
    
    user_entries = [
        (r'Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo', 'Enabled', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 'PreInstalledAppsEnabled', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 'OemPreInstalledAppsEnabled', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 'ContentDeliveryAllowed', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 'SubscribedContentEnabled', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\InputPersonalization', 'RestrictImplicitInkCollection', 1, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\InputPersonalization', 'RestrictImplicitTextCollection', 1, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Siuf\Rules', 'PeriodInNanoSeconds', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\CurrentVersion\SearchSettings', 'IsMSACloudSearchEnabled', 0, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\CurrentVersion\SearchSettings', 'IsDeviceSearchHistoryEnabled', 0, reg.REG_DWORD),
    ]
    
    for path, name, value, vtype in user_entries:
        try:
            key = reg.CreateKeyEx(reg.HKEY_CURRENT_USER, path, 0, reg.KEY_WRITE)
            reg.SetValueEx(key, name, 0, vtype, value)
            reg.CloseKey(key)
        except:
            pass

def get_backup_data():
    backup = {}
    backup['registry'] = []
    return backup

def restore(backup_data):
    if not backup_data:
        return
