import subprocess
import winreg as reg
import sys
import os
import ctypes
import uuid

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

def run_command(cmd):
    try:
        subprocess.run(cmd, shell=True, check=False, capture_output=True)
    except:
        pass

def set_registry_key(root, path, name, value, value_type=reg.REG_DWORD):
    try:
        key = reg.CreateKeyEx(root, path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, name, 0, value_type, value)
        reg.CloseKey(key)
    except:
        pass

def delete_registry_key(root, path, name):
    try:
        key = reg.OpenKey(root, path, 0, reg.KEY_SET_VALUE)
        reg.DeleteValue(key, name)
        reg.CloseKey(key)
    except:
        pass

def get_active_nic_guids():
    guids = []
    try:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces")
        i = 0
        while True:
            try:
                subkey_name = reg.EnumKey(key, i)
                guids.append(subkey_name)
                i += 1
            except:
                break
        reg.CloseKey(key)
    except:
        pass
    return guids

def enable_large_pages_privilege():
    import win32security
    import win32api
    import ntsecuritycon
    try:
        token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY)
        privs = [(win32security.LookupPrivilegeValue(None, ntsecuritycon.SE_LOCK_MEMORY_NAME), win32security.SE_PRIVILEGE_ENABLED)]
        win32security.AdjustTokenPrivileges(token, False, privs)
    except:
        pass

def enable_msi_for_devices():
    key_path = r"SYSTEM\CurrentControlSet\Enum\PCI"
    try:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path)
        i = 0
        while True:
            try:
                device_id = reg.EnumKey(key, i)
                device_key_path = f"{key_path}\\{device_id}\\Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties"
                set_registry_key(reg.HKEY_LOCAL_MACHINE, device_key_path, "MSISupported", 1)
                i += 1
            except:
                break
        reg.CloseKey(key)
    except:
        pass

run_command("powercfg /setacvalueindex scheme_current sub_processor CPMINCORES 100")
run_command("powercfg /setdcvalueindex scheme_current sub_processor CPMINCORES 100")
run_command("powercfg /setacvalueindex scheme_current sub_processor PROCTHROTTLING 0")
run_command("powercfg /setdcvalueindex scheme_current sub_processor PROCTHROTTLING 0")
run_command("powercfg /setacvalueindex scheme_current sub_processor IDLEPROMOTE 100")
run_command("powercfg /setdcvalueindex scheme_current sub_processor IDLEPROMOTE 100")
run_command("powercfg /setacvalueindex scheme_current sub_processor IDLEDEMOTE 100")
run_command("powercfg /setdcvalueindex scheme_current sub_processor IDLEDEMOTE 100")
run_command("powercfg -setacvalueindex scheme_current sub_disk 0b2d69d7-a2a1-449c-9680-f91c70521c60 0")
run_command("powercfg -setdcvalueindex scheme_current sub_disk 0b2d69d7-a2a1-449c-9680-f91c70521c60 0")
run_command("powercfg -setacvalueindex scheme_current sub_disk dab60367-53fe-4fbc-825e-521d069d2456 0")
run_command("powercfg -setdcvalueindex scheme_current sub_disk dab60367-53fe-4fbc-825e-521d069d2456 0")
run_command("powercfg -setacvalueindex scheme_current sub_pciExpress ee12f906-d277-404b-b6da-e5fa1a576df5 0")
run_command("powercfg -setdcvalueindex scheme_current sub_pciExpress ee12f906-d277-404b-b6da-e5fa1a576df5 0")
run_command("powercfg /setactive scheme_current")

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\PriorityControl", "Win32PrioritySeparation", 26)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\PriorityControl", "IRQ8Priority", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games", "Affinity", "High", reg.REG_SZ)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games", "Priority", 6)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games", "Scheduling Category", "High", reg.REG_SZ)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games", "SFIO Priority", "High", reg.REG_SZ)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games", "GPU Priority", 8)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "NetworkThrottlingIndex", 0xFFFFFFFF)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "SystemResponsiveness", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "NoLazyMode", 1)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583", "ValueMax", 100)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583", "ValueMin", 100)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Kernel", "ThreadQuantum", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel", "DisableWaitLoopOptimization", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel", "ProcessPriorityClass", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel", "EnableTimerCoalescing", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel", "TimerLatencyTolerance", 0)

run_command("sc config SysMain start=disabled")
run_command("sc stop SysMain")
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters", "EnablePrefetcher", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters", "EnableSuperfetch", 0)

enable_large_pages_privilege()

try:
    drive = os.environ['SystemDrive']
    run_command(f"wmic pagefileset where name=\"{drive}\\pagefile.sys\" set InitialSize=4096,MaximumSize=4096")
except:
    pass

run_command("powershell.exe -Command Disable-MMAgent -mc")
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "DisablePageCombining", 1)

nic_guids = get_active_nic_guids()
for guid in nic_guids:
    interface_path = f"SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid}"
    set_registry_key(reg.HKEY_LOCAL_MACHINE, interface_path, "TCPNoDelay", 1)
    set_registry_key(reg.HKEY_LOCAL_MACHINE, interface_path, "TcpAckFrequency", 1)
    set_registry_key(reg.HKEY_LOCAL_MACHINE, interface_path, "TcpDelAckTicks", 0)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Psched", "NonBestEffortLimit", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "MaxFreeTcbs", 65536)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "MaxFlows", 8192)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\QoS", "NonBestEffortLimit", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters", "Size", 3)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters", "MinFreeConnections", 100)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters", "MaxCmds", 255)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters", "DisableBandwidthThrottling", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet", "EnableActiveProbing", 0)

run_command("netsh int tcp set global congestionprovider=dctcp")
run_command("powershell.exe -Command Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Interrupt Moderation' -DisplayValue 'Disabled'")
run_command("powershell.exe -Command Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Packet Coalescing' -DisplayValue 'Disabled'")
run_command("powershell.exe -Command Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Flow Control' -DisplayValue 'Disabled'")
run_command("powershell.exe -Command Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Jumbo Packet' -DisplayValue 'Disabled'")
run_command("powershell.exe -Command Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Energy Efficient Ethernet' -DisplayValue 'Disabled'")
run_command("powershell.exe -Command Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Green Ethernet' -DisplayValue 'Disabled'")
run_command("powershell.exe -Command Set-NetAdapterAdvancedProperty -Name '*' -DisplayName 'Power Saving Mode' -DisplayValue 'Disabled'")
run_command("netsh int tcp set global autotuninglevel=normal")
run_command("netsh int tcp set global ecncapability=disabled")
run_command("netsh int tcp set global chimney=disabled")
run_command("netsh int tcp set global rss=disabled")
run_command("netsh int tcp set global netdma=enabled")
run_command("netsh int tcp set global dca=enabled")
run_command("netsh int tcp set global timestamps=disabled")
run_command("netsh int tcp set global nonsackrttresiliency=disabled")
run_command("netsh int tcp set global initialrto=2000")
run_command("netsh int tcp set global minrto=300")

run_command("bcdedit /deletevalue useplatformclock")
run_command("bcdedit /set useplatformtick yes")
run_command("bcdedit /set disabledynamictick yes")
run_command("bcdedit /set tscsyncpolicy Enhanced")
run_command("bcdedit /set x2apicpolicy Enable")

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "FeatureSettingsOverride", 3)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "FeatureSettingsOverrideMask", 3)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\DeviceGuard", "EnableVirtualizationBasedSecurity", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity", "Enabled", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\CI\Policy", "VerifiedAndReputablePolicyState", 0)

enable_msi_for_devices()

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\Dwm", "OverlayTestMode", 5)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\Dwm", "EnablePreemption", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\Dwm", "EnableWindowPoser", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\DWM", "EnableBufferCompression", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\DWM", "FlushUINonBlocking", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\DWM", "DisableDirtyRegionOptimization", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\DWM", "DisableMPO", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers", "HwSchMode", 2)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "DisableFullscreenOptimizations", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers", "PlatformAutoPowerDown", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power", "DefaultD3TransitionLatency", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler", "EnablePreemption", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler", "MaxFrameBuffers", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler", "ForceDmaMode", 1)

run_command("fsutil behavior set disable8dot3 1")
run_command("fsutil behavior set disablelastaccess 1")
run_command("fsutil behavior set encryptpagingfile 0")
run_command("fsutil behavior set mftzone 4")
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\FileSystem", "FsUtilDeregisterMaxWaitTime", 0)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Mouclass\Parameters", "MouseDataQueueSize", 50)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\kbdclass\Parameters", "KeyboardDataQueueSize", 50)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USB", "DisableSelectiveSuspend", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", "Start", 4)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\FileSystem", "NtfsMemoryUsage", 2)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "DisablePagingExecutive", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "LargeSystemCache", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "IoPageLockLimit", 0x8000000)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "LowMemoryThreshold", 0)

services = [
    "DiagTrack", "WSearch", "Spooler", "MapsBroker", "XboxGipSvc", "PcaSvc", "WerSvc", "DoSvc",
    "DeviceAssociationService", "DPS", "WdiServiceHost", "WdiSystemHost", "WdNisSvc", "WinDefend",
    "WdBoot", "WdFilter", "SysMain", "CDPSvc", "ClipSVC", "UsoSvc", "TabletInputService",
    "RetailDemo", "Fax", "PhoneSvc", "lfsvc", "AJRouter", "AllJoynRouter", "MessagingService",
    "PimIndexMaintenanceSvc", "OneSyncSvc", "WalletService", "wisvc", "WpcMonSvc", "WpnUserService",
    "RemoteRegistry", "RemoteAccess", "shpamsvc", "tzautoupdate", "SgrmBroker", "SmsRouter",
    "SharedAccess", "SvcTopology", "XblGameSave", "NvStreamSvc", "NvContainerLocalSystem",
    "TimeBrokerSvc", "BthAvctpSvc", "DisplayEnhancementService"
]
for s in services:
    run_command(f"sc config {s} start=disabled")
    run_command(f"sc stop {s}")

set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", "AppCaptureEnabled", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_Enabled", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications", "GlobalUserDisabled", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\InterruptManagement", "DisableInterruptSteering", 1)
run_command("wmic nicconfig where TcpipNetbiosOptions=0 or TcpipNetbiosOptions=1 call SetTcpipNetbios 2")
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "MaxUserPort", 65534)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "TcpTimedWaitDelay", 30)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control", "SvcHostSplitThresholdInKB", 33554432)

set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects", "VisualFXSetting", 2)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", "ListviewAlphaSelect", "0", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", "TaskbarAnimations", "0", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "EnableTransparency", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", "MenuShowDelay", "0", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseSpeed", "0", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseThreshold1", "0", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseThreshold2", "0", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", "CursorRefresh", 0)

run_command("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
run_command("powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61")
run_command("fsutil behavior set disabledeletenotify 0")
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\FTH", "Enabled", 0)
run_command("powercfg -h off")
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Power", "HiberbootEnabled", 0)

set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Accessibility\StickyKeys", "Flags", "506", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Accessibility\Keyboard Response", "Flags", "122", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Accessibility\ToggleKeys", "Flags", "58", reg.REG_SZ)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options", "MitigationOptions", 0x2000000000000, reg.REG_QWORD)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\NVIDIA Corporation\Global\NVTweak", "FlipQueueSize", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\nvlddmkm\Global\NvTweak", "ShaderCacheSize", 10240)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000", "KMD_EspressoOffload", 0)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Configuration Manager", "EnablePeriodicBackup", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "AllowCortana", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching", "SearchOrderConfig", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Device Metadata", "PreventDeviceMetadataFromNetwork", 1)

run_command("powershell.exe -Command Get-AppxPackage *Microsoft.Windows.Client.WebExperience* | Remove-AppxPackage")

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "EnableSmartScreen", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection", "DisableRealtimeMonitoring", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager", "ProtectionMode", 0)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SubscribedContent-338389Enabled", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SubscribedContent-338388Enabled", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SubscribedContent-310093Enabled", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SubscribedContent-338393Enabled", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SilentInstalledAppsEnabled", 0)

set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", "AutoEndTasks", "1", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", "HungAppTimeout", "1000", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", "WaitToKillAppTimeout", "1000", reg.REG_SZ)
set_registry_key(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", "LowLevelHooksTimeout", "1000", reg.REG_SZ)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control", "WaitToKillServiceTimeout", "2000", reg.REG_SZ)

set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "SeparateProcess", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer", "NoRecentDocsHistory", 1)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowRecent", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowFrequent", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\CloudContent", "DisableSoftLanding", 1)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SystemPaneSuggestionsEnabled", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "Start_TrackProgs", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\People", "PeopleBand", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "DisableSearchBoxSuggestions", 1)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Search", "SearchboxTaskbarMode", 1)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "DefaultTTL", 64)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo", "Enabled", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\AdvertisingInfo", "Enabled", 0)
set_registry_key(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowSyncProviderNotifications", 0)

run_command("del /q/f/s %TEMP%\\*")
run_command("del /q/f/s C:\\Windows\\Temp\\*")

run_command("fltmc unload wdfilter")

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583", "Attributes", 2)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\75b0ae3f-bce0-45a7-8c89-c9611c25e100", "Attributes", 2)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\5d76a2ca-e8c0-402f-a133-2158492d58ad", "ValueMax", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\619b7505-003b-4e82-b7a6-4dd29c300971", "ValueMax", 100)

run_command("powershell.exe -Command Disable-MMAgent -MemoryCompression")
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "NonPagedPoolQuota", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "PagedPoolQuota", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "PoolUsageMaximum", 60)

run_command("fsutil behavior set disableencryption 1")
run_command("fsutil behavior set memoryusage 2")
run_command("fsutil behavior set quotanotify 0")
run_command("fsutil behavior set bugcheckoncorrupt 0")
run_command("fsutil behavior set symlinkevaluation L2L:1 L2R:0 R2R:0 R2L:0")

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "TcpNumConnections", 0x00FFFFFE)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "GlobalMaxTcpWindowSize", 65535)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "TcpNoDelay", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Dnscache\Parameters", "MaxCacheTtl", 86400)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Dnscache\Parameters", "MaxNegativeCacheTtl", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\AFD\Parameters", "FastSendDatagramThreshold", 1024)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\AFD\Parameters", "DefaultReceiveWindow", 65535)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\AFD\Parameters", "DefaultSendWindow", 65535)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\stornvme\Parameters", "EnableHMB", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\stornvme\Parameters", "EnableWakeOnCompletion", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\stornvme\Parameters\Device", "IoQueueDepth", 256)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\stornvme\Parameters\Device", "NumberOfIoQueues", 16)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\dmio\Parameters", "DmaAlignment", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\storahci\Parameters", "EnableDMA", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Terminal Server", "fMinimizeLatency", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Terminal Server\Winstations\RDP-Tcp", "fDisableCrtShftAlt", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Terminal Server\Winstations\RDP-Tcp", "fColorDepth", 1)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers", "TdrDelay", 60)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power", "DefaultPowerPolicy", 2)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Power", "RMPowerPositioning", 2)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows Media Foundation\Platform", "EnableFrameServerMode", 0)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\storahci\Parameters\Device", "LPM", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\0012ee47-9041-4b5d-9b77-535fba8b1442\d639518a-e56d-4345-8af2-b9f32fb26109", "ValueMax", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\0012ee47-9041-4b5d-9b77-535fba8b1442\d639518a-e56d-4345-8af2-b9f32fb26109", "ValueMin", 0)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\mouclass\Parameters", "ThreadPriority", 31)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\kbdclass\Parameters", "ThreadPriority", 31)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\mouclass\Parameters", "PowerDeviceEnable", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\kbdclass\Parameters", "PowerDeviceEnable", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\mouclass\Parameters", "WppRecorder_TraceGuid", 0)

run_command("bcdedit /debug off")
run_command("bcdedit /set bootlog no")

tasks_to_disable = [
    r"\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser",
    r"\Microsoft\Windows\Application Experience\ProgramDataUpdater",
    r"\Microsoft\Windows\Autochk\Proxy",
    r"\Microsoft\Windows\Customer Experience Improvement Program\Consolidator",
    r"\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip",
    r"\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector",
    r"\Microsoft\Windows\Maintenance\WinSAT",
    r"\Microsoft\Windows\Maps\MapsToastTask",
    r"\Microsoft\Windows\Maps\MapsUpdateTask",
    r"\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem",
    r"\Microsoft\Windows\Shell\FamilySafetyMonitor",
    r"\Microsoft\Windows\Shell\FamilySafetyRefresh",
    r"\Microsoft\Windows\Windows Error Reporting\QueueReporting",
]
for task in tasks_to_disable:
    run_command(f'schtasks /Change /TN "{task}" /Disable')

run_command("bcdedit /set useplatformclock false")
run_command("bcdedit /set highestmode yes")
run_command("bcdedit /set configaccesspolicy DisallowMmConfig")
run_command("bcdedit /set linearaddress57 OptOut")
run_command("bcdedit /set increaseuserva 268435456")

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "DisablePagingKernel", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "SessionPoolSize", 128)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management", "SessionViewSize", 256)

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "TcpInitialRTT", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "Tcp1323Opts", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", "DisableTaskOffload", 0)
run_command("netsh int tcp set supplemental template=internet congestionprovider=bbr2")
run_command("netsh int tcp set global rsc=disabled")
run_command("netsh int tcp set global rstmaxsynretransmit=2")

set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\nvlddmkm\Parameters", "RmGpcPowerManagementMode", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\NVIDIA Corporation\Global\NVTweak\PowerMizer", "PerfLevelSrc", 3322)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000", "DisableDynamicPstate", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000", "KMD_EnableLatencyTolerance", 1)

run_command('powershell -Command "Get-PnpDevice -Class USB | Where-Object {$_.InstanceId -like \'*HUB*\'} | ForEach-Object { Set-ItemProperty -Path \'HKLM:\\SYSTEM\\CurrentControlSet\\Enum\\$($_.InstanceId)\\Device Parameters\' -Name \'DeviceSelectiveSuspended\' -Value 0 -ErrorAction SilentlyContinue}"')
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\stornvme\Parameters\Device", "AutonomousPowerStateTransitionLatencyTolerance", 0)

run_command("powershell.exe -Command Disable-MMAgent -PageCombining")
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583", "Attributes", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\238c9fa8-0aad-41ed-83f4-97be242c8f20", "Attributes", 0)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\Windows Error Reporting", "Disabled", 1)
set_registry_key(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\Windows Error Reporting", "DontSendAdditionalData", 1)