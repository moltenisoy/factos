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


def apply_power():
    """Optimizaciones de energía: Desactivar ahorro de energía y throttling"""
    if os.name != "nt":
        sys.exit(1)

    # Create backup before applying power optimizations
    backup_info = create_full_backup("power")
    
    # Apply power optimizations
    run("Reg.exe add \\\"%%n\\\" /v \\\"AutoPowerSaveModeEnabled\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"NicAutoPowerSaver\\\" /t REG_SZ /d \\\"2\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"EnableWakeOnLan\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"S5WakeOnLan\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"EnablePME\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"EnableGreenEthernet\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"EnableSavePowerNow\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"EnablePowerManagement\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"PowerDownPll\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"PowerSavingMode\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"ReduceSpeedOnPowerDown\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"EnableConnectedPowerGating\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"GigaLite\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"ULPMode\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"WakeOnDisconnect\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"*WakeOnMagicPacket\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"*WakeOnPattern\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"WakeOnLink\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\hidusb\\\\Parameters\\\" /v \\\"EnablePowerManagement\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("Reg.exe add \\\"%%n\\\" /v \\\"EnabledynamicPowerGating\\\" /t REG_SZ /d \\\"0\\\" /f")
    run("reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%a\\\\Device Parameters\\\" /v EnhancedPowerManagementEnabled /t REG_DWORD /d 0 /f")
    run("reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%a\\\\Device Parameters\\\" /v AllowIdleIrpInD3 /t REG_DWORD /d 0 /f")
    run("\"schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\FileHistory\\\\File History (maintenance mode")
    run("\"schtasks /change /tn \\\"\\\\Microsoft\\\\Windows\\\\FileHistory\\\\File History (triggered backup")
    run("reg add \\\"HKLM\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\FileHistory\\\" /v \\\"Disabled\\\" /t REG_DWORD /d 1 /f")
    run("reg add \\\"HKLM\\\\SOFTWARE\\\\Microsoft\\\\PolicyManager\\\\default\\\\System\\\\TurnOffFileHistory\\\" /v \\\"value\\\" /t REG_DWORD /d 1 /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\storahci\\\\Parameters\\\\Device\\\" /v \\\"EnableDIPM\\\" /t REG_DWORD /d 0 /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\storahci\\\\Parameters\\\\Device\\\" /v \\\"EnableHIPM\\\" /t REG_DWORD /d 0 /f")
    run("reg.exe add \\\"HKEY_LOCAL_MACHINE\\\\SYSTEM\\\\ControlSet001\\\\Control\\\\Power\\\" /V \\\"HibernateEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\storahci\\\\Parameters\\\\Device\\\" /v \\\"EnableDIPM\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\storahci\\\\Parameters\\\\Device\\\" /v \\\"EnableHIPM\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Power\\\" /v \\\"HibernateEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%s\\\\Device Parameters\\\" /v EnhancedPowerManagementEnabled /t REG_DWORD /d 0 /f")
    run("reg.exe add \\\"HKEY_LOCAL_MACHINE\\\\System\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"EnhancedPowerManagementEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("Reg.exe add \\\"HKLM\\\\System\\\\CurrentControlSet\\\\Enum\\\\%%a\\\\Device Parameters\\\" /v \\\"EnhancedPowerManagementEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%a\\\\Device Parameters\\\" /f /v \\\"EnhancedPowerManagementEnabled\\\" /t REG_DWORD /d 0")
    run("reg add \\\"HKLM\\\\System\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"EnhancedPowerManagementEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"EnhancedPowerManagementEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("REG ADD \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%a\\\\Device Parameters\\\" /F /V \\\"EnhancedPowerManagementEnabled\\\" /T REG_DWORD /d 0")
    run("reg.exe add \\\"HKLM\\\\SYSTEM\\\\ControlSet001\\\\Enum\\\\%%a\\\\Device Parameters\\\" /v EnhancedPowerManagementEnabled /t REG_DWORD /d 00000000 /f")
    run("reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%s\\\\Device Parameters\\\" /v AllowIdleIrpInD3 /t REG_DWORD /d 0 /f")
    run("reg.exe add \\\"HKEY_LOCAL_MACHINE\\\\System\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"AllowIdleIrpInD3\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg.exe add \\\"HKEY_LOCAL_MACHINE\\\\System\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"D3ColdSupported\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("Reg.exe add \\\"HKLM\\\\System\\\\CurrentControlSet\\\\Enum\\\\%%a\\\\Device Parameters\\\" /v \\\"AllowIdleIrpInD3\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("REG ADD \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\FileHistory\\\" /v \\\"Disabled\\\" /t REG_DWORD /d 1 /f")
    run("REG ADD \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\PolicyManager\\\\default\\\\System\\\\TurnOffFileHistory\\\" /v \\\"value\\\" /t REG_DWORD /d 1 /f")
    run("REG DELETE \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Schedule\\\\TaskCache\\\\Tree\\\\Microsoft\\\\Windows\\\\FileHistory\\\" /f")
    run("reg add \\\"%%s\\\" /v \\\"EnableIdlePowerManagement\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"%%s\\\" /v \\\"IdlePowerManagement\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%a\\\\Device Parameters\\\" /f /v \\\"AllowIdleIrpInD3\\\" /t REG_DWORD /d 0")
    run("reg add \\\"HKLM\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\FileHistory\\\" /v \\\"Enabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Session Manager\\\\Power\\\" /v \\\"HiberbootEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("REG ADD \\\"%%a\\\" /F /V \\\"EnableHIPM\\\" /T REG_DWORD /d \\\"0\\\"")
    run("REG ADD \\\"%%a\\\" /F /V \\\"EnableDIPM\\\" /T REG_DWORD /d \\\"0\\\"")
    run("REG ADD \\\"%%a\\\" /F /V \\\"EnableHDDParking\\\" /T REG_DWORD /d \\\"0\\\"")
    run("REG ADD \\\"%%a\\\" /F /V \\\"EnableALPM\\\" /T REG_DWORD /d \\\"0\\\"")
    run("reg add \\\"HKLM\\\\System\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"AllowIdleIrpInD3\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\System\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"D3ColdSupported\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"AllowIdleIrpInD3\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%i\\\\Device Parameters\\\" /v \\\"D3ColdSupported\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("REG ADD \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Enum\\\\%%a\\\\Device Parameters\\\" /F /V \\\"AllowIdleIrpInD3\\\" /T REG_DWORD /d 0")
    run("reg.exe add \\\"HKLM\\\\SYSTEM\\\\ControlSet001\\\\Enum\\\\%%a\\\\Device Parameters\\\" /v AllowIdleIrpInD3 /t REG_DWORD /d 00000000 /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"ThermalThrottling\\\" /t REG_DWORD /d \\\"0\\\" /f")
    run("reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Power\\\" /v \\\"PowerThrottlingOff\\\" /t REG_DWORD /d \\\"1\\\" /f")
    run("\"schtasks /Change /TN \\\"Microsoft\\\\Windows\\\\FileHistory\\\\File History (maintenance mode")
    run("\"schtasks /end /tn \\\"\\\\Microsoft\\\\Windows\\\\FileHistory\\\\File History (maintenance mode")


def get_backup_data():
    return {'backup_created': True}


def restore_from_backup_data(backup_data):
    if not backup_data:
        return
