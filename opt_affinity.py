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


def apply_affinity():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d 26 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v IRQ8Priority /t REG_DWORD /d 1 /f',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-Process -Name \"csrss\" -ErrorAction SilentlyContinue; if ($p) { foreach ($proc in $p) { try { $proc.ProcessorAffinity = [IntPtr]1 } catch {} } } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-Process -Name \"winlogon\" -ErrorAction SilentlyContinue; if ($p) { foreach ($proc in $p) { try { $proc.ProcessorAffinity = [IntPtr]1 } catch {} } } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-Process -Name \"wininit\" -ErrorAction SilentlyContinue; if ($p) { foreach ($proc in $p) { try { $proc.ProcessorAffinity = [IntPtr]1 } catch {} } } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-Process -Name \"services\" -ErrorAction SilentlyContinue; if ($p) { foreach ($proc in $p) { try { $proc.ProcessorAffinity = [IntPtr]1 } catch {} } } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-Process -Name \"lsass\" -ErrorAction SilentlyContinue; if ($p) { foreach ($proc in $p) { try { $proc.ProcessorAffinity = [IntPtr]1 } catch {} } } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-Process -Name \"smss\" -ErrorAction SilentlyContinue; if ($p) { foreach ($proc in $p) { try { $proc.ProcessorAffinity = [IntPtr]1 } catch {} } } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $numCores = (Get-CimInstance Win32_Processor).NumberOfLogicalProcessors; $allCoresMask = [IntPtr]([Math]::Pow(2, $numCores) - 1); Get-Process | Where-Object { $_.MainWindowHandle -ne 0 -and $_.Name -notmatch \"^(System|Idle|Registry|smss|csrss|wininit|winlogon|services|lsass)$\" } | ForEach-Object { try { $_.ProcessorAffinity = $allCoresMask } catch {} } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $numCores = (Get-CimInstance Win32_Processor).NumberOfLogicalProcessors; $bgMask = [IntPtr]([Math]::Pow(2, [Math]::Floor($numCores / 2)) - 1); Get-Process | Where-Object { $_.MainWindowHandle -eq 0 -and $_.Name -notmatch \"^(System|Idle|Registry|smss|csrss|wininit|winlogon|services|lsass|svchost|MsMpEng)$\" } | ForEach-Object { try { $_.ProcessorAffinity = $bgMask; $_.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::BelowNormal } catch {} } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-Process -Name \"audiodg\" -ErrorAction SilentlyContinue; if ($p) { $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High } }"',
        r'PowerShell -ExecutionPolicy Bypass -Command "& { $p = Get-Process -Name \"svchost\" -ErrorAction SilentlyContinue; if ($p) { foreach ($proc in $p) { try { $proc.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::Normal } catch {} } } }"',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v Priority /t REG_DWORD /d 6 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Scheduling Category" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "SFIO Priority" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v Priority /t REG_DWORD /d 6 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v "Scheduling Category" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v "SFIO Priority" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Audio" /v "Background Only" /t REG_SZ /d False /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe\PerfOptions" /v CpuPriorityClass /t REG_DWORD /d 4 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe\PerfOptions" /v IoPriority /t REG_DWORD /d 3 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\audiodg.exe\PerfOptions" /v CpuPriorityClass /t REG_DWORD /d 3 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\audiodg.exe\PerfOptions" /v IoPriority /t REG_DWORD /d 3 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\dwm.exe\PerfOptions" /v CpuPriorityClass /t REG_DWORD /d 3 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\dwm.exe\PerfOptions" /v IoPriority /t REG_DWORD /d 3 /f',
    ]

    for cmd in commands:
        run(cmd)


if __name__ == "__main__":
    apply_affinity()
