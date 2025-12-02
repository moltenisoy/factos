import subprocess
import os
import sys


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
    """Optimizaciones de almacenamiento: SSD, disco, indexación y compresión"""
    if os.name != "nt":
        sys.exit(1)

    # Disable disk defragmentation
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Defrag\\ScheduledDefrag\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\DiskCleanup\\SilentCleanup\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Defrag\\ScheduledOptimize\" /disable")
    run("schtasks /Change /TN \"Microsoft\\Windows\\Defrag\\ScheduledDefrag\" /Disable")
    run("schtasks /Change /TN \"Microsoft\\Windows\\DiskCleanup\\SilentCleanup\" /Disable")

    # Disable disk diagnostics
    run("schtasks /change /tn \"\\Microsoft\\Windows\\DiskFootprint\\Diagnostics\" /Disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector\" /Disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticResolver\" /Disable")

    # Disable Superfetch/Prefetch
    run("powershell -NoProfile -ExecutionPolicy Bypass -Command \"Disable-MMAgent -ApplicationLaunchPrefetching -OperationAPI -PageCombining -ApplicationPreLaunch\"")
    run("schtasks /Change /TN \"Microsoft\\Windows\\Sysmain\\ResPriStaticDbSync\" /Disable")
    run("schtasks /Change /TN \"Microsoft\\Windows\\Sysmain\\WsSwapAssessmentTask\" /Disable")
    run("sc config \"SysMain\" start=disabled")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\SysMain\" /v \"Start\" /t REG_DWORD /d \"4\" /f")

    # Disable Windows Search indexing
    run("sc config \"WSearch\" start=disabled")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\WSearch\" /v \"Start\" /t REG_DWORD /d \"4\" /f")

    # Disable low disk space checks
    run("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"NoLowDiskSpaceChecks\" /t REG_DWORD /d 1 /f")
    run("Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"NoLowDiskSpaceChecks\" /t REG_DWORD /d \"1\" /f")
    run("REG ADD \"HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"NoLowDiskSpaceChecks\" /t REG_DWORD /d 1 /f")
    run("Reg.exe add \"HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\\Windows.SystemToast.LowDisk\" /v \"Enabled\" /t REG_DWORD /d \"0\" /f")

    # Disable disk quota
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\DiskQuota\" /v \"Enforce\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\DiskQuota\" /v \"Enable\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\DiskQuota\" /v \"LogEventOverLimit\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\DiskQuota\" /v \"LogEventOverThreshold\" /t REG_DWORD /d 0 /f")

    # Optimize disk timeout
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Disk\" /v \"TimeOutValue\" /t REG_DWORD /d \"200\" /f")

    # Enable write cache for better performance
    run("Reg.exe add \"%%k\\Device Parameters\\Disk\" /v UserWriteCacheSetting /t REG_DWORD /d 1 /f")
    run("Reg.exe add \"%%k\\Device Parameters\\Disk\" /v CacheIsPowerProtected /t REG_DWORD /d 1 /f")

    # Disable NTFS last access time stamps (improves SSD performance)
    run("fsutil behavior set disablelastaccess 1")

    # Disable 8.3 file name creation (improves performance)
    run("fsutil behavior set disable8dot3 1")

    # Disable memory compression
    run("powershell -NoProfile -ExecutionPolicy Bypass -Command \"Disable-MMAgent -MemoryCompression\"")

    # Disable paging executive
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"DisablePagingExecutive\" /t REG_DWORD /d 1 /f")

    # Disable hibernation (saves disk space)
    run("powercfg /h off")

    # Disable system restore points creation
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore\" /v \"DisableSR\" /t REG_DWORD /d 1 /f")

    # Optimize NTFS
    run("fsutil behavior set mftzone 2")
