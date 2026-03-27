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


def apply_gpu_deep():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v HwSchMode /t REG_DWORD /d 2 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v PlatformSupportMiracast /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler" /v EnablePreemption /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler" /v VsyncIdleTimeout /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler" /v PreemptionLevel /t REG_DWORD /d 100 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v Priority /t REG_DWORD /d 6 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Scheduling Category" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "SFIO Priority" /t REG_SZ /d High /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Latency Sensitive" /t REG_SZ /d True /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Background Only" /t REG_SZ /d False /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Clock Rate" /t REG_DWORD /d 10000 /f',
        r'reg add "HKCU\System\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\System\GameConfigStore" /v GameDVR_FSEBehaviorMode /t REG_DWORD /d 2 /f',
        r'reg add "HKCU\System\GameConfigStore" /v GameDVR_HonorUserFSEBehaviorMode /t REG_DWORD /d 1 /f',
        r'reg add "HKCU\System\GameConfigStore" /v GameDVR_DXGIHonorFSEWindowsCompatible /t REG_DWORD /d 1 /f',
        r'reg add "HKCU\System\GameConfigStore" /v GameDVR_EFSEFeatureFlags /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\GameDVR" /v AllowGameDVR /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v LargePageMinimum /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\DirectX" /v D3D12_ENABLE_UNSAFE_COMMAND_BUFFER_REUSE /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\DirectX" /v D3D11_MULTITHREADED /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\DirectX\UserGpuPreferences" /v DirectXUserGlobalSettings /t REG_SZ /d "VRROptimizeEnable=0;SwapEffectUpgradeEnable=1;" /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\DirectX\UserGpuPreferences" /v DirectXUserGlobalSettings /t REG_SZ /d "VRROptimizeEnable=0;SwapEffectUpgradeEnable=1;" /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v Disable_OverlayDSoundHW /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v DisableBlockWrite /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v RMHdcpKeygroupMode /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /v EnableMsHybrid /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global" /v NvCplEnableHdr /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global\NvCplApi\Policies" /v OverclockingAllowed /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global\NvCplApi\Policies" /v PowerSavingMode /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global\Startup\SendTelemetryData" /v 0 /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v Composition /t REG_DWORD /d 1 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v EnableAeroPeek /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v AlwaysHibernateThumbnails /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\DWM" /v UseWindowFrameStagingBuffer /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\DWM" /v OverlayTestMode /t REG_DWORD /d 5 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v UseOLEDTaskbarTransparency /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v TaskbarAnimations /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\DCI" /v Timeout /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v DisableAutoAcpiGpuDetection /t REG_DWORD /d 0 /f',
    ]

    for cmd in commands:
        run(cmd)


if __name__ == "__main__":
    apply_gpu_deep()
