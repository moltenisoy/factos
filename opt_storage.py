import subprocess
import os
import sys
from backup_mgr_comprehensive import create_comprehensive_backup, restore_from_comprehensive_backup


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

    # Extract all commands to pass to backup system
    commands_to_apply = [
        r"""schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\Defrag\\\\ScheduledDefrag\\\" /disable""",
        r"""schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\DiskCleanup\\\\SilentCleanup\\\" /disable""",
        r"""schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\Defrag\\\\ScheduledOptimize\\\" /disable""",
        r"""schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\EDP\\\\StorageCardEncryption Task\\\" /disable""",
        r"""reg delete \\\"HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\MyComputer\\\\DefragPath\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\Software\\\\Policies\\\\Microsoft\\\\Windows\\\\EnhancedStorageDevices\\\" /v \\\"TCGSecurityActivationDisabled\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\MyComputer\\\\DefragPath\\\" /f""",
        r"""REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Manage\\\" /f""",
        r"""REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Migration\\\" /f""",
        r"""REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Migration_Cancel\\\" /f""",
        r"""REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Migration_Confirmation\\\" /f""",
        r"""REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Migration_Error\\\" /f""",
        r"""REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\SystemSettings\\\\SettingId\\\\SystemSettings_Maps_Storage_Options\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"QueueDepth\\\" /t REG_DWORD /d \\\"32\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"CompletionQueueSize\\\" /t REG_DWORD /d \\\"64\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"SubmissionQueueSize\\\" /t REG_DWORD /d \\\"64\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"IdlePowerMode\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"AutonomousPowerStateTransition\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"IoQueuesPerCore\\\" /t REG_DWORD /d \\\"2\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"MaxIoQueues\\\" /t REG_DWORD /d \\\"16\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"EnableLatencyControl\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"WriteCacheEnabled\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"EnableVolatileWriteCache\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"ForcedPhysicalSectorSizeInBytes\\\" /t REG_MULTI_SZ /d \\\"* 4096\\\" /f""",
        r"""reg add \\\"HKLM\\\\System\\\\ControlSet001\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"DmaRemappingCompatible\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKLM\\\\System\\\\ControlSet001\\\\Services\\\\stornvme\\\\Parameters\\\" /v \\\"DmaRemappingCompatible\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKLM\\\\Software\\\\Policies\\\\Microsoft\\\\Windows\\\\EnhancedStorageDevices\\\" /v \\\"TCGSecurityActivationDisabled\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"DisableThrottling\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\Defrag\\\\ScheduledDefrag\\\" /Disable""",
        r"""schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\DiskCleanup\\\\SilentCleanup\\\" /Disable""",
        r"""schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\Storage Tiers Management\\\\Storage Tiers Management Initialization\\\" /Disable""",
        r"""schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\Sysmain\\\\ResPriStaticDbSync\\\" /Disable""",
        r"""schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\Sysmain\\\\WsSwapAssessmentTask\\\" /Disable""",
        r"""schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\WOF\\\\WIM-Hash-Management\\\" /Disable""",
        r"""schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\WOF\\\\WIM-Hash-Validation\\\" /Disable""",
        r"""REG ADD \\\"HKEY_LOCAL_MACHINE\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\WSearch\\\" /v \\\"Start\\\" /t REG_DWORD /d 3 /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\SysMain\\\" /v \\\"Start\\\" /t REG_DWORD /d \\\"4\\\" /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\WSearch\\\" /v \\\"Start\\\" /t REG_DWORD /d \\\"4\\\" /f""",
    ]
    
    # Create comprehensive backup BEFORE applying optimizations
    print(f"Creating comprehensive backup for storage...")
    backup_info = create_comprehensive_backup("storage", commands_to_apply)
    print(f"Backup created: {{backup_info['backed_up_items']}} items backed up")
    print(f"Backup directory: {{backup_info['backup_directory']}}")
    
    # Now apply all optimizations
    print(f"Applying storage optimizations...")
    for cmd in commands_to_apply:
        run(cmd)
    
    print(f"{category_name.title()} optimizations completed!")
    return backup_info


def get_backup_data():
    return {{'backup_created': True}}


def restore_from_backup_data(backup_dir):
    if not backup_dir:
        return False
    return restore_from_comprehensive_backup(backup_dir)
