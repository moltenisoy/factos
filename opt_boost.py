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


def apply_boost():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c',
        r'powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 be337238-0d82-4146-a960-4f3749d470c7 2',
        r'powercfg /setdcvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 be337238-0d82-4146-a960-4f3749d470c7 2',
        r'powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 100',
        r'powercfg /setdcvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 100',
        r'powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 bc5038f7-23e0-4960-96da-33abaf5935ec 100',
        r'powercfg /setdcvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 bc5038f7-23e0-4960-96da-33abaf5935ec 100',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v PowerThrottlingOff /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" /v PowerThrottlingOff /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v DistributeTimers /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v GlobalTimerResolutionRequests /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d 26 /f',
        r'PowerShell -ExecutionPolicy Bypass -Command "Get-Process | Where-Object { $_.MainWindowHandle -ne 0 } | ForEach-Object { try { $_.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High } catch {} }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "Get-Process | Where-Object { $_.MainWindowHandle -eq 0 -and $_.Name -notmatch \"^(System|Idle|Registry|smss|csrss|wininit|winlogon|services|lsass|svchost|MsMpEng)$\" } | ForEach-Object { try { $_.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::BelowNormal } catch {} }"',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v Priority /t REG_DWORD /d 6 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Scheduling Category" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "SFIO Priority" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Background Only" /t REG_SZ /d False /f',
    ]

    for cmd in commands:
        run(cmd)


if __name__ == "__main__":
    apply_boost()
