import subprocess
import os
import sys

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except Exception:
        pass

def apply_power():
    """Optimizaciones de energía: CPU, rendimiento y gestión de energía"""
    if os.name != "nt":
        sys.exit(1)

    # Set high performance power plan
    run("powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
    
    # Disable USB selective suspend
    run("powercfg -setacvalueindex scheme_current 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0")
    run("powercfg -setdcvalueindex scheme_current 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0")
    
    # Disable PCI Express Link State Power Management
    run("powercfg -setacvalueindex scheme_current 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 0")
    run("powercfg -setdcvalueindex scheme_current 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 0")
    
    # Set processor power management to maximum performance
    run("powercfg -setacvalueindex scheme_current 54533251-82be-4824-96c1-47b60b740d00 bc5038f7-23e0-4960-96da-33abaf5935ec 100")
    run("powercfg -setacvalueindex scheme_current 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 100")
    
    # Disable hard disk sleep
    run("powercfg -setacvalueindex scheme_current 0012ee47-9041-4b5d-9b77-535fba8b1442 6738e2c4-e8a5-4a42-b16a-e040e769756e 0")
    run("powercfg -setdcvalueindex scheme_current 0012ee47-9041-4b5d-9b77-535fba8b1442 6738e2c4-e8a5-4a42-b16a-e040e769756e 0")
    
    # Disable sleep after time
    run("powercfg -change -standby-timeout-ac 0")
    run("powercfg -change -standby-timeout-dc 0")
    
    # Disable hibernation
    run("powercfg /h off")
    
    # Disable monitor timeout
    run("powercfg -change -monitor-timeout-ac 0")
    run("powercfg -change -monitor-timeout-dc 0")
    
    # Apply power settings
    run("powercfg -setactive scheme_current")
    
    # Disable power throttling
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling\" /v \"PowerThrottlingOff\" /t REG_DWORD /d 1 /f")
    
    # Disable CPU parking (all cores active)
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\0cc5b647-c1df-4637-891a-dec35c318583\" /v \"ValueMax\" /t REG_DWORD /d 0 /f")
    
    # Disable network adapter power management
    run("powershell -NoProfile -ExecutionPolicy Bypass -Command \"Get-NetAdapter | Disable-NetAdapterPowerManagement -WakeOnMagicPacket:$false -WakeOnPattern:$false -DeviceSleepOnDisconnect:$false -SelectiveSuspend:$false -ArpOffload:$false -NSOffload:$false -D0PacketCoalescing:$false -RsnRekeyOffload:$false -NoRestart -ErrorAction SilentlyContinue\"")
    run("Reg.exe add \"%%n\" /v \"AutoPowerSaveModeEnabled\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"NicAutoPowerSaver\" /t REG_SZ /d \"2\" /f")
    run("Reg.exe add \"%%n\" /v \"EnableSavePowerNow\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"EnablePowerManagement\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"PowerDownPll\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"PowerSavingMode\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"ReduceSpeedOnPowerDown\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"EnableConnectedPowerGating\" /t REG_SZ /d \"0\" /f")
    
    # Disable USB power management
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\hidusb\\Parameters\" /v \"EnablePowerManagement\" /t REG_DWORD /d \"0\" /f")
    
    # Disable fast startup (can cause issues)
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power\" /v \"HiberbootEnabled\" /t REG_DWORD /d 0 /f")
    
    # Performance registry settings
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"ClearPageFileAtShutdown\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"LargeSystemCache\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"SecondLevelDataCache\" /t REG_DWORD /d 0 /f")
    
    # Disable dynamic tick
    run("bcdedit /set disabledynamictick yes")
    
    # Use all cores for boot
    run("bcdedit /set numproc 0")
    
    # Performance boot settings
    run("bcdedit /set quietboot yes")
    run("bcdedit /timeout 3")
