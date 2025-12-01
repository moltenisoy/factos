import subprocess
import winreg as reg
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

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
            "HKEY_USERS": reg.HKEY_USERS
        }
        
        root_key = root_keys.get(root, reg.HKEY_LOCAL_MACHINE)
        key = reg.CreateKeyEx(root_key, subkey, 0, reg.KEY_WRITE | reg.KEY_WOW64_64KEY)
        reg.SetValueEx(key, name, 0, value_type, value)
        reg.CloseKey(key)
    except:
        pass

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

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

run_cmd('schtasks /change /Disable /tn "NVIDIA GeForce Experience SelfUpdate_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}"')

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

set_reg("HKLM\\CurrentControlSet\\Control\\GraphicsDrivers\\Scheduler", "EnablePreemption", 0, reg.REG_DWORD)

run_cmd('sc config FrameServer start=disabled')
run_cmd('sc config FrameServerMonitor start=demand')
run_cmd('sc stop FrameServer')

result = subprocess.run('wmic path Win32_VideoController get PNPDeviceID', shell=True, capture_output=True, text=True)
for line in result.stdout.splitlines():
    if "VEN_" in line:
        device_id = line.strip()
        set_reg(f"HKLM\\SYSTEM\\CurrentControlSet\\Enum\\{device_id}\\Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties", "MSISupported", 1, reg.REG_DWORD)

result = subprocess.run('wmic path Win32_VideoController get PNPDeviceID', shell=True, capture_output=True, text=True)
for line in result.stdout.splitlines():
    if "PCI\\VEN_" in line:
        set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrLimitCount", 256, reg.REG_DWORD)
        set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers", "TdrLimitTime", 60, reg.REG_DWORD)
        break

set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "DisableAGPSupport", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "UseNonLocalVidMem", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "UseNonLocalVidMem", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "EnablePrintScreen", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "VGABuffer", 21181233, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "VGABuffer", 21181233, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "EmulationOnly", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers", "ForceRgbRasterizer", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "FlipNoVsync", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "DisableAGPSupport", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "UseNonLocalVidMem", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "UseNonLocalVidMem", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "DisableDDSCAPSInDDSD", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "DisableDDSCAPSInDDSD", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "EmulationOnly", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "EmulatePointSprites", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "EmulatePointSprites", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers", "ForceRgbRasterizer", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "EmulateStateBlocks", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "EmulateStateBlocks", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "EnableDebugging", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "FullDebug", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "DisableDM", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "EnableMultimonDebugging", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "LoadDebugRuntime", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers", "EnumReference", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers", "EnumReference", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers", "EnumSeparateMMX", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers", "EnumSeparateMMX", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers", "EnumRamp", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers", "EnumRamp", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers", "EnumNullDevice", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers", "EnumNullDevice", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "FewVertices", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "FewVertices", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "DisableMMX", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "DisableMMX", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "DisableMMX", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "DisableMMX", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "MMX Fast Path", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "MMX Fast Path", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "MMXFastPath", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "MMXFastPath", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "UseMMXForRGB", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "UseMMXForRGB", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers", "UseMMXForRGB", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers", "UseMMXForRGB", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "ForceNoSysLock", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "ForceNoSysLock", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "DisableMultithreading", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "MaxPreRenderedFrames", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "MaxFrameLatency", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "EnableUltralowLatencyMode", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "LowLatencyMode", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "ForceVSYNC", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "DisableTimeoutDetection", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "DisableThreadedOptimization", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "HighPriorityGPU", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "DisableHardwareAcceleration", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "EnablePrintScreen", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "VGABuffer", 21181233, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "VGABuffer", 21181233, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectMusic", "VGABuffer", 21181233, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectMusic", "VGABuffer", 21181233, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "DisableDP2", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "DisableDP2", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\Direct3D", "D3DXDoNotMute", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "D3DXDoNotMute", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D", "FlipNoVsync", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\DirectDraw", "ModeXOnly", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw", "ModeXOnly", 0, reg.REG_DWORD)

set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm", "DisablePreemption", 1, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm", "DisableCudaContextPreemption", 1, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm\\Parameters", "ThreadPriority", 31, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm\\FTS", "EnableRID61684", 1, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm\\Global\\NVTweak", "DisplayPowerSaving", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\ControlSet001\\Services\\nvlddmkm\\Global\\NVTweak", "DisplayPowerSaving", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\ControlSet001\\Services\\nvlddmkm", "EnableMidBufferPreemption", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm", "0x112493bd", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm", "0x11e91a61", 4294967295, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\ControlSet001\\Services\\nvlddmkm", "DisableCudaContextPreemption", 1, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\ControlSet001\\Services\\nvlddmkm", "EnableMidGfxPreemption", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\ControlSet001\\Services\\nvlddmkm", "EnableMidGfxPreemptionVGPU", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\ControlSet001\\Services\\nvlddmkm", "EnableMidBufferPreemptionForHighTdrTimeout", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\ControlSet001\\Services\\nvlddmkm", "ComputePreemption", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\ControlSet001\\Services\\nvlddmkm", "DisablePreemption", 1, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm", "DisableWriteCombining", 1, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm", "EnableCEPreemption", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm", "DisablePreemptionOnS3S4", 1, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Services\\nvlddmkm", "ComputePreemption", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\NVTweak", "DisplayPowerSaving", 0, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "DisableCudaContextPreemption", 1, reg.REG_DWORD)
set_reg("HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "DisablePreemptionOnS3S4", 1, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\FTS", "EnableRID66610", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\FTS", "EnableRID64640", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\NVIDIA Corporation\\Global\\FTS", "EnableRID44231", 0, reg.REG_DWORD)

set_reg("HKCU\\Software\\Microsoft\\GameBar", "UseNexusForGameBarEnabled", 0, reg.REG_DWORD)
set_reg("HKCU\\Software\\Microsoft\\GameBar", "GameDVR_Enabled", 0, reg.REG_DWORD)
set_reg("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR", "AppCaptureEnabled", 0, reg.REG_DWORD)
set_reg("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR", "AudioCaptureEnabled", 0, reg.REG_DWORD)
set_reg("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR", "CursorCaptureEnabled", 0, reg.REG_DWORD)
set_reg("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR", "HistoricalCaptureEnabled", 0, reg.REG_DWORD)
set_reg("HKCU\\System\\GameConfigStore", "GameDVR_Enabled", 0, reg.REG_DWORD)
set_reg("HKLM\\Software\\Policies\\Microsoft\\Windows\\GameDVR", "AllowgameDVR", 0, reg.REG_DWORD)
set_reg("HKCU\\System\\GameConfigStore", "GameDVR_FSEBehaviorMode", 2, reg.REG_DWORD)
set_reg("HKCU\\System\\GameConfigStore", "GameDVR_HonorUserFSEBehaviorMode", 1, reg.REG_DWORD)
set_reg("HKCU\\System\\GameConfigStore", "GameDVR_DXGIHonorFSEWindowsCompatible", 1, reg.REG_DWORD)
set_reg("HKCU\\System\\GameConfigStore", "GameDVR_EFSEFeatureFlags", 0, reg.REG_DWORD)
set_reg("HKCU\\System\\GameConfigStore", "GameDVR_FSEBehavior", 2, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR", "AllowGameDVR", 0, reg.REG_DWORD)
set_reg("HKLM\\SOFTWARE\\Microsoft\\PolicyManager\\default\\ApplicationManagement\\AllowGameDVR", "value", 0, reg.REG_DWORD)
set_reg("HKCU\\SOFTWARE\\Microsoft\\GameBar", "ShowStartupPanel", 0, reg.REG_DWORD)
set_reg("HKCU\\SOFTWARE\\Microsoft\\GameBar", "GamePanelStartupTipIndex", 3, reg.REG_DWORD)
set_reg("HKCU\\SOFTWARE\\Microsoft\\GameBar", "AllowAutoGameMode", 0, reg.REG_DWORD)
set_reg("HKCU\\SOFTWARE\\Microsoft\\GameBar", "AutoGameModeEnabled", 1, reg.REG_DWORD)
set_reg("HKEY_USERS\\.DEFAULT\\System\\GameConfigStore", "GameDVR_Enabled", 0, reg.REG_DWORD)
set_reg("HKEY_USERS\\.DEFAULT\\System\\GameConfigStore", "GameDVR_FSEBehaviorMode", 2, reg.REG_DWORD)
set_reg("HKEY_USERS\\.DEFAULT\\System\\GameConfigStore", "GameDVR_HonorUserFSEBehaviorMode", 1, reg.REG_DWORD)
set_reg("HKEY_USERS\\.DEFAULT\\System\\GameConfigStore", "GameDVR_DXGIHonorFSEWindowsCompatible", 1, reg.REG_DWORD)
set_reg("HKEY_USERS\\.DEFAULT\\System\\GameConfigStore", "GameDVR_EFSEFeatureFlags", 0, reg.REG_DWORD)
set_reg("HKEY_USERS\\.DEFAULT\\System\\GameConfigStore", "GameDVR_FSEBehavior", 2, reg.REG_DWORD)
set_reg("HKEY_USERS\\.DEFAULT\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR", "AppCaptureEnabled", 0, reg.REG_DWORD)
set_reg("HKEY_USERS\\.DEFAULT\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR", "HistoricalCaptureEnabled", 0, reg.REG_DWORD)

try:
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameBar_LearnMore", 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameBar_LearnMore")
    reg.CloseKey(key)
except:
    pass

try:
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameBar_NexusButton", 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameBar_NexusButton")
    reg.CloseKey(key)
except:
    pass

try:
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameBar_Toggle", 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameBar_Toggle")
    reg.CloseKey(key)
except:
    pass

try:
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameDVR_HardwareEncoder", 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameDVR_HardwareEncoder")
    reg.CloseKey(key)
except:
    pass

try:
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameDVRHeader_LearnMore", 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameDVRHeader_LearnMore")
    reg.CloseKey(key)
except:
    pass

try:
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameDVRHeader_OpenFolder", 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\SystemSettings\\SettingId\\SystemSettings_Gaming_GameDVRHeader_OpenFolder")
    reg.CloseKey(key)
except:
    pass

try:
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\WindowsRuntime\\ActivatableClassId\\Windows.Gaming.UI.GameBar", 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\WindowsRuntime\\ActivatableClassId\\Windows.Gaming.UI.GameBar")
    reg.CloseKey(key)
except:
    pass

try:
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\WindowsRuntime\\ActivatableClassId\\Windows.Gaming.GameBar.PresenceServer.Internal.PresenceWriter", 0, reg.KEY_ALL_ACCESS)
    reg.DeleteKey(reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\WindowsRuntime\\ActivatableClassId\\Windows.Gaming.GameBar.PresenceServer.Internal.PresenceWriter")
    reg.CloseKey(key)
except:
    pass

run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.Print3D\' | Remove-AppxPackage"')
run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Windows.Print3D\' | Remove-AppxPackage"')
run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.3DBuilder\' | Remove-AppxPackage"')
run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.Microsoft3DViewer\' | Remove-AppxPackage"')
run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.HEIFImageExtension\' | Remove-AppxPackage"')
run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.VP9VideoExtensions\' | Remove-AppxPackage"')
run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.WebMediaExtensions\' | Remove-AppxPackage"')
run_cmd('PowerShell -ExecutionPolicy Unrestricted -Command "Get-AppxPackage \'Microsoft.WebpImageExtension\' | Remove-AppxPackage"')
run_cmd('PowerShell -Command "Get-AppxPackage *3DBuilder* | Remove-AppxPackage"')