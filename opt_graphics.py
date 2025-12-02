import subprocess
import winreg as reg
import json

BACKUP_FILE = 'backup_opt_graphics.json'

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def set_reg(path, name, value, value_type):
    try:
        parts = path.split('\\', 1)
        root = parts[0]
        subkey = parts[1] if len(parts) > 1 else ""
        
        root_keys = {
            "HKLM": reg.HKEY_LOCAL_MACHINE,
            "HKCU": reg.HKEY_CURRENT_USER,
            "HKEY_LOCAL_MACHINE": reg.HKEY_LOCAL_MACHINE,
            "HKEY_CURRENT_USER": reg.HKEY_CURRENT_USER,
        }
        
        root_key = root_keys.get(root, reg.HKEY_LOCAL_MACHINE)
        key = reg.CreateKeyEx(root_key, subkey, 0, reg.KEY_WRITE)
        reg.SetValueEx(key, name, 0, value_type, value)
        reg.CloseKey(key)
    except Exception:
        pass

def apply_all():
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "Disable_OverlayDSQualityEnhancement", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "IncreaseFixedSegment", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "AdaptiveVsyncEnable", 0, reg.REG_DWORD)
    set_reg("HKCU\\Software\\Microsoft\\Windows\\DWM", "EnableAnimations", 0, reg.REG_DWORD)
    set_reg("HKCU\\Software\\Microsoft\\Windows\\DWM", "EnableTransparency", 0, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows\\Dwm", "OverlayTestMode", 5, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows\\Dwm", "ForceDoubleBuffer", 1, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows\\Dwm", "MaxQueuedBuffers", 2, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows\\Dwm", "EnablePerProcessSystemScheduling", 1, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", "NetworkThrottlingIndex", 4294967295, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", "SystemResponsiveness", 0, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", "AlwaysOn", 1, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile", "NoLazyMode", 1, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Audio", "Scheduling Category", "High", reg.REG_SZ)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Playback", "Scheduling Category", "High", reg.REG_SZ)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Capture", "Scheduling Category", "High", reg.REG_SZ)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Distribution", "Scheduling Category", "High", reg.REG_SZ)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Pro Audio", "Scheduling Category", "High", reg.REG_SZ)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Window Manager", "Scheduling Category", "High", reg.REG_SZ)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\DisplayPostProcessing", "Scheduling Category", "High", reg.REG_SZ)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\DisplayPostProcessing", "Latency Sensitive", "True", reg.REG_SZ)
    set_reg("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Terminal Services", "fAllowUnsolicited", 0, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Terminal Services", "fAllowToGetHelp", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "DisableWriteCombining", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "RMDisablePostL2Compression", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "RmDisableRegistryCaching", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "HwSchMode", 2, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "PlatformSupportMiracast", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "RmGpsPsEnablePerCpuCoreDpc", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "MonitorLatencyTolerance", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "MonitorRefreshLatencyTolerance", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "EnablePreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "GPUPreemptionLevel", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "ComputePreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "EnableMidGfxPreemptionVGPU", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "EnableMidBufferPreemptionForHighTdrTimeout", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "EnableAsyncMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "EnableSCGMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "PerfAnalyzeMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "EnableMidGfxPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "EnableMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "EnableCEPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrLevel", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrDelay", 10, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrDdiDelay", 60, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrLimitTime", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrLimitCount", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "DxMaxFrameLatency", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "MaxFrameLatency", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "ForceThreadedRendering", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "DisableMultithreading", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "DisableHWAcceleration", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "GraphicsPreemption", 2, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "DisableCudaContextPreemption", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "DisablePreemptionOnS3S4", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "RMDisablePostL2Compression", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "RmDisableRegistryCaching", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "RmGpsPsEnablePerCpuCoreDpc", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "DisableWriteCombining", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "MonitorLatencyTolerance", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "MonitorRefreshLatencyTolerance", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "EnablePreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "ComputePreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "EnableMidGfxPreemptionVGPU", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "EnableMidBufferPreemptionForHighTdrTimeout", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "EnableAsyncMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "EnableSCGMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "PerfAnalyzeMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "EnableMidGfxPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "EnableMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "EnableCEPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "GPUPreemptionLevel", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "DisableCudaContextPreemption", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Power", "DisablePreemptionOnS3S4", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "PlatformSupportMiracast", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "RMDisablePostL2Compression", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "RmDisableRegistryCaching", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "RmGpsPsEnablePerCpuCoreDpc", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "DisableWriteCombining", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnablePreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "GPUPreemptionLevel", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnableAsyncMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnableMidGfxPreemptionVGPU", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnableMidBufferPreemptionForHighTdrTimeout", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnableSCGMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "PerfAnalyzeMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnableMidGfxPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnableMidBufferPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnableCEPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "ComputePreemptionLevel", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "DisableCudaContextPreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "DisablePreemptionOnS3S4", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "DisablePreemption", 1, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnablePreemption", 0, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrLimitCount", 256, reg.REG_DWORD)
    set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrLimitTime", 60, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "DisableAGPSupport", 0, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "UseNonLocalVidMem", 1, reg.REG_DWORD)
    set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "UseNonLocalVidMem", 1, reg.REG_DWORD)
    run_cmd('schtasks /change /Disable /tn "NVIDIA GeForce Experience SelfUpdate_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"')
    run_cmd('sc config FrameServer start=disabled')
    run_cmd('sc config FrameServerMonitor start=demand')
    run_cmd('sc stop FrameServer')
    run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.Print3D\' | Remove-AppxPackage"')
    run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Windows.Print3D\' | Remove-AppxPackage"')
    run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.3DBuilder\' | Remove-AppxPackage"')
    run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.Microsoft3DViewer\' | Remove-AppxPackage"')
    run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.HEIFImageExtension\' | Remove-AppxPackage"')
    run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.VP9VideoExtensions\' | Remove-AppxPackage"')
    run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.WebMediaExtensions\' | Remove-AppxPackage"')
    run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.WebpImageExtension\' | Remove-AppxPackage"')
    run_cmd('PowerShell -Command "Get-AppxPackage *3DBuilder* | Remove-AppxPackage"')


def get_backup_data():
    return {'backup_created': True}

def restore_from_backup(backup_data):
    if not backup_data:
        return
