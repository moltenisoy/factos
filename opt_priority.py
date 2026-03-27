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


def apply_priority():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d 26 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v IRQ8Priority /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v Priority /t REG_DWORD /d 6 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Scheduling Category" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "SFIO Priority" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Background Only" /t REG_SZ /d False /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v Affinity /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Clock Rate" /t REG_DWORD /d 10000 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Latency Sensitive" /t REG_SZ /d True /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v "GPU Priority" /t REG_DWORD /d 8 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v Priority /t REG_DWORD /d 6 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v "Scheduling Category" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v "SFIO Priority" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v "Background Only" /t REG_SZ /d False /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v LargeSystemCache /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v DisablePagingExecutive /t REG_DWORD /d 1 /f',
        r'PowerShell -ExecutionPolicy Bypass -Command "Get-Process | Where-Object { $_.MainWindowHandle -ne 0 } | ForEach-Object { try { $_.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High } catch {} }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "Get-Process | Where-Object { $_.MainWindowHandle -eq 0 -and $_.Name -notmatch \"^(System|Idle|Registry|smss|csrss|wininit|winlogon|services|lsass|svchost|MsMpEng)$\" } | ForEach-Object { try { $_.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::BelowNormal } catch {} }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-ItemProperty -Path \"HKLM:\SYSTEM\CurrentControlSet\Control\PriorityControl\"; if ($null -eq $p.IRQ8Priority) { New-ItemProperty -Path \"HKLM:\SYSTEM\CurrentControlSet\Control\PriorityControl\" -Name IRQ8Priority -Value 1 -PropertyType DWORD -Force } }"',
    ]

    for cmd in commands:
        run(cmd)


if __name__ == "__main__":
    apply_priority()
