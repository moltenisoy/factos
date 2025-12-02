import subprocess
import winreg as reg

def apply():
    registry_entries = [
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'Disable_OverlayDSQualityEnhancement', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'IncreaseFixedSegment', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'AdaptiveVsyncEnable', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'EnableUlps', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'PP_ThermalAutoThrottlingEnable', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'DisableUVDPowerGatingDynamic', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'DisableVCEPowerGating', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'KMD_DeLagEnabled', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'KMD_EnableComputePreemption', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'PreferSystemMemoryContiguous', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'D3PCLatency', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'F1TransitionLatency', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'LOWLATENCY', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'Node3DLowLatency', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'PciLatencyTimerControl', 32, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000', 'RMDeepL1EntryLatencyUsec', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler', 'DisableWriteCombining', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'RMDisablePostL2Compression', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'RmDisableRegistryCaching', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'HwSchMode', 2, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'PlatformSupportMiracast', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'RmGpsPsEnablePerCpuCoreDpc', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'MonitorLatencyTolerance', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'MonitorRefreshLatencyTolerance', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'EnablePreemption', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'GPUPreemptionLevel', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'ComputePreemption', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'TdrLevel', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'TdrDelay', 10, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'DxMaxFrameLatency', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Control\GraphicsDrivers', 'MaxFrameLatency', 1, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\Dwm', 'OverlayTestMode', 5, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\Dwm', 'ForceDoubleBuffer', 1, reg.REG_DWORD),
        (r'SOFTWARE\Microsoft\Windows\Dwm', 'MaxQueuedBuffers', 2, reg.REG_DWORD),
    ]
    
    for path, name, value, vtype in registry_entries:
        try:
            key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
            reg.SetValueEx(key, name, 0, vtype, value)
            reg.CloseKey(key)
        except:
            pass
    
    user_entries = [
        (r'Software\Microsoft\Windows\DWM', 'EnableAnimations', 0, reg.REG_DWORD),
        (r'Software\Microsoft\Windows\DWM', 'EnableTransparency', 0, reg.REG_DWORD),
    ]
    
    for path, name, value, vtype in user_entries:
        try:
            key = reg.CreateKeyEx(reg.HKEY_CURRENT_USER, path, 0, reg.KEY_WRITE)
            reg.SetValueEx(key, name, 0, vtype, value)
            reg.CloseKey(key)
        except:
            pass

def get_backup_data():
    backup = {}
    backup['registry'] = []
    return backup

def restore(backup_data):
    if not backup_data:
        return
