import subprocess
import winreg as reg

def apply():
    services_config = [
        ('workfolderssvc', 'disabled'),
        ('BthAvctpSvc', 'disabled'),
        ('BthHFSrv', 'disabled'),
        ('BTAGService', 'disabled'),
        ('bthserv', 'disabled'),
        ('Netlogon', 'disabled'),
        ('Netman', 'disabled'),
        ('WwanSvc', 'disabled'),
        ('wcncsvc', 'disabled'),
        ('DPS', 'disabled'),
        ('WdiServiceHost', 'disabled'),
        ('WdiSystemHost', 'disabled'),
        ('PcaSvc', 'disabled'),
        ('diagsvc', 'disabled'),
        ('SSDPSRV', 'disabled'),
        ('UmRdpService', 'disabled'),
        ('Spooler', 'disabled'),
        ('FontCache', 'disabled'),
        ('FontCache3.0.0.0', 'disabled'),
        ('stisvc', 'disabled'),
        ('Wecsvc', 'disabled'),
        ('PrintNotify', 'disabled'),
        ('WSearch', 'disabled'),
        ('SysMain', 'disabled'),
        ('lfsvc', 'disabled'),
    ]
    
    for service, start_type in services_config:
        try:
            subprocess.run(f'sc config "{service}" start={start_type}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(f'sc stop "{service}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
    
    tasks = [
        r'Microsoft\Windows\Defrag\ScheduledDefrag',
        r'Microsoft\Windows\Diagnosis\RecommendedTroubleshootingScanner',
        r'Microsoft\Windows\Diagnosis\Scheduled',
        r'Microsoft\Windows\DiskCleanup\SilentCleanup',
        r'Microsoft\Windows\FileHistory\File History (maintenance mode)',
        r'Microsoft\Windows\Maintenance\WinSAT',
        r'Microsoft\Windows\RemoteAssistance\RemoteAssistanceTask',
        r'Microsoft\Windows\Servicing\StartComponentCleanup',
        r'Microsoft\Windows\Storage Tiers Management\Storage Tiers Management Initialization',
        r'Microsoft\Windows\Time Synchronization\SynchronizeTime',
        r'Microsoft\Windows\Windows Filtering Platform\BfeOnServiceStartTypeChange',
        r'Microsoft\Windows\WDI\ResolutionHost',
        r'Microsoft\Windows\Customer Experience Improvement Program\Consolidator',
        r'Microsoft\Windows\Application Experience\StartupAppTask',
    ]
    
    for task in tasks:
        try:
            subprocess.run(f'schtasks /Change /TN "{task}" /Disable', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

def get_backup_data():
    backup = {}
    backup['services'] = []
    return backup

def restore(backup_data):
    if not backup_data:
        return
