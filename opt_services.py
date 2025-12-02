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


def apply_services():
    """Optimizaciones de servicios: Deshabilitar servicios innecesarios de Windows"""
    if os.name != "nt":
        sys.exit(1)

    # Bluetooth services
    run("sc config \"BthAvctpSvc\" start=disabled")
    run("sc config \"BthHFSrv\" start=disabled")
    run("sc config \"BTAGService\" start=manual")
    run("sc config \"bthserv\" start=manual")
    run("sc config \"BluetoothUserService\" start=demand")

    # Work folders
    run("sc config \"workfolderssvc\" start=disabled")

    # Update services
    run("sc config \"UsoSvc\" start=disabled")
    run("sc config \"wuauserv\" start=disabled")
    run("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\UsoSvc\" /v Start /t reg_dword /d 4 /f")
    run("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\wuauserv\" /v Start /t reg_dword /d 4 /f")

    # Print services
    run("sc config \"PrintNotify\" start=disabled")
    run("sc config \"Spooler\" start=disabled")

    # Remote services
    run("sc config \"RemoteAccess\" start=disabled")
    run("sc config \"RemoteRegistry\" start=disabled")
    run("sc config \"SessionEnv\" start=disabled")
    run("sc config \"TermService\" start=disabled")
    run("sc config \"UmRdpService\" start=disabled")

    # Windows search and indexing
    run("sc config \"WSearch\" start=disabled")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\WSearch\" /v \"Start\" /t REG_DWORD /d \"4\" /f")

    # Superfetch/SysMain
    run("sc config \"SysMain\" start=disabled")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\SysMain\" /v \"Start\" /t REG_DWORD /d \"4\" /f")

    # Windows Defender (if not needed)
    run("sc config \"WdNisSvc\" start=disabled")
    run("sc config \"WinDefend\" start=disabled")
    run("sc config \"SecurityHealthService\" start=disabled")

    # Xbox services
    run("sc config \"XblAuthManager\" start=disabled")
    run("sc config \"XblGameSave\" start=disabled")
    run("sc config \"XboxGipSvc\" start=disabled")
    run("sc config \"XboxNetApiSvc\" start=disabled")

    # Tablet and touch services
    run("sc config \"TabletInputService\" start=disabled")
    run("sc config \"TouchKeyboard\" start=disabled")

    # Diagnostics services
    run("sc config \"DPS\" start=disabled")
    run("sc config \"WdiServiceHost\" start=disabled")
    run("sc config \"WdiSystemHost\" start=disabled")

    # Sensor services
    run("sc config \"SensorDataService\" start=disabled")
    run("sc config \"SensorService\" start=disabled")
    run("sc config \"SensrSvc\" start=disabled")

    # Geolocation
    run("sc config \"lfsvc\" start=disabled")

    # Biometrics
    run("sc config \"WbioSrvc\" start=disabled")

    # Windows Connect Now
    run("sc config \"wcncsvc\" start=disabled")

    # Smart card
    run("sc config \"SCardSvr\" start=disabled")
    run("sc config \"ScDeviceEnum\" start=disabled")
    run("sc config \"SCPolicySvc\" start=disabled")

    # Parental controls
    run("sc config \"WpcMonSvc\" start=disabled")

    # Maps
    run("sc config \"MapsBroker\" start=disabled")

    # Downloaded Maps Manager
    run("sc config \"dmwappushservice\" start=disabled")

    # Fax
    run("sc config \"Fax\" start=disabled")

    # Phone service
    run("sc config \"PhoneSvc\" start=disabled")

    # Retail demo
    run("sc config \"RetailDemo\" start=disabled")

    # SSDP Discovery
    run("sc config \"SSDPSRV\" start=disabled")

    # Windows Insider service
    run("sc config \"wisvc\" start=disabled")

    # Diagnostic execution service
    run("sc config \"diagsvc\" start=disabled")

    # Windows Image Acquisition
    run("sc config \"stisvc\" start=disabled")

    # Program Compatibility Assistant
    run("sc config \"PcaSvc\" start=disabled")

    # Scheduled tasks optimization
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Application Experience\\ProgramDataUpdater\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Autochk\\Proxy\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Defrag\\ScheduledDefrag\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Device Information\\Device\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\DiskFootprint\\Diagnostics\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Maintenance\\WinSAT\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Maps\\MapsUpdateTask\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Windows Error Reporting\\QueueReporting\" /disable")
