import subprocess
import os
import sys
from backup_mgr import create_full_backup, restore_from_backup


def run(cmd):
    try:
        subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False)
    except Exception:
        pass


def apply_storage():
    """Optimizaciones de almacenamiento: SSD, indexación y rendimiento de disco"""
    if os.name != "nt":
        sys.exit(1)

    # Create backup before applying storage optimizations
    backup_info = create_full_backup("storage")
    
    # Apply storage optimizations
    run("schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\Defrag\\\\ScheduledDefrag\\\" /disable")
    run("schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\DiskCleanup\\\\SilentCleanup\\\" /disable")
    run("schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\Defrag\\\\ScheduledOptimize\\\" /disable")
    run("schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\EDP\\\\StorageCardEncryption Task\\\" /disable")
    run("reg delete \\\"HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\MyComputer\\\\DefragPath\\\" /f")
    run("Reg.exe add \\\"HKLM\\\\Software\\\\Policies\\\\Microsoft\\\\Windows\\\\EnhancedStorageDevices\\\" /v \\\"TCGSecurityActivationDisabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\MyComputer\\\\DefragPath\\\" /f")
    run("REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Manage\\\" /f")
    run("REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Migration\\\" /f")
    run("REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Migration_Cancel\\\" /f")
    run("REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Migration_Confirmation\\\" /f")
    run("REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Migration_Error\\\" /f")
    run("REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Options\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"QueueDepth\\\" /t REG_DWORD /d \\\"32\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"CompletionQueueSize\\\" /t REG_DWORD /d \\\"64\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"SubmissionQueueSize\\\" /t REG_DWORD /d \\\"64\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"IdlePowerMode\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"AutonomousPowerStateTransition\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"IoQueuesPerCore\\\" /t REG_DWORD /d \\\"2\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"MaxIoQueues\\\" /t REG_DWORD /d \\\"16\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"EnableLatencyControl\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"WriteCacheEnabled\\\" /t REG_DWORD /d \\\"1\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"EnableVolatileWriteCache\\\" /t REG_DWORD /d \\\"1\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"ForcedPhysicalSectorSizeInBytes\\\" /t REG_MULTI_SZ /d \\\"* 4096\\\" /f")
    run("reg add \\\"HKLM\\\\System\\\\ControlSet001\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"DmaRemappingCompatible\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\System\\\\ControlSet001\\\\Services\\\\stornvme\\\\Parameters\\\" /v \\\"DmaRemappingCompatible\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\Software\\\\Policies\\\\Microsoft\\\\Windows\\\\EnhancedStorageDevices\\\" /v \\\"TCGSecurityActivationDisabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"DisableThrottling\\\" /t REG_DWORD /d \\\"1\\\" /f")
    run("schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\Defrag\\\\ScheduledDefrag\\\" /Disable")
    run("schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\DiskCleanup\\\\SilentCleanup\\\" /Disable")
    run("schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\Storage Tiers Management\\\\Storage Tiers Management Initialization\\\" /Disable")
    run("schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\Sysmain\\\\ResPriStaticDbSync\\\" /Disable")
    run("schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\Sysmain\\\\WsSwapAssessmentTask\\\" /Disable")
    run("schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\WOF\\\\WIM-Hash-Management\\\" /Disable")
    run("schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\WOF\\\\WIM-Hash-Validation\\\" /Disable")
    run("REG ADD \\\"HKEY_LOCAL_MACHINE\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\WSearch\\\" /v \\\"Start\\\" /t REG_DWORD /d 3 /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\SysMain\\\" /v \\\"Start\\\" /t REG_DWORD /d \\\"4\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\WSearch\\\" /v \\\"Start\\\" /t REG_DWORD /d \\\"4\\\" /f")


def get_backup_data():
    return {'backup_created': True}


def restore_from_backup_data(backup_data):
    if not backup_data:
        return
