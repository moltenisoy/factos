import subprocess
import os
import sys

def run_command(command, shell=True, suppress_output=True):
    try:
        if suppress_output:
            subprocess.run(command, shell=shell, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        else:
            subprocess.run(command, shell=shell, check=False)
    except Exception:
        pass

def get_cpu_cores():
    try:
        result = subprocess.run('wmic cpu get NumberOfCores /value | find "="', shell=True, capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if '=' in line:
                return int(line.split('=')[1].strip())
    except:
        return 4
    return 4

def network_optimizations():
    cpu_cores = get_cpu_cores()
    if cpu_cores >= 6:
        task_offload = "Disabled"
        dto_value = "1"
        nic_value = "0"
    else:
        task_offload = "Enabled"
        dto_value = "0"
        nic_value = "1"
    run_command('netsh int teredo set state disabled')
    run_command('netsh int tcp set heuristics Disabled')
    run_command(f'netsh int ip set global taskoffload={task_offload}')
    run_command('netsh winsock reset')
    run_command('netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent')
    run_command('netsh interface tcp set global initialrto=2000')
    run_command('netsh advfirewall set allprofiles state off')
    run_command('netsh int tcp set global autotuninglevel=normal')
    run_command('netsh int tcp set global rss=enabled')
    run_command('netsh int tcp set global chimney=enabled')
    run_command('netsh int tcp set global netdma=enabled')
    run_command('netsh int tcp set global dca=enabled')
    run_command('netsh int tcp set global congestionprovider=ctcp')
    run_command('netsh int tcp set heuristics disabled')
    run_command('netsh int tcp set global timestamps=disabled')
    run_command('netsh int tcp set global fastopen=enabled')
    run_command('netsh Int tcp set global nonsackrttresiliency=disabled')
    run_command('netsh Int tcp set global netdma=enabled')
    run_command('netsh Int tcp set global congestionprovider=ctcp')
    run_command('netsh Int tcp set global dca=enabled')
    run_command('netsh int tcp set global autotuninglevel=disabled')
    run_command('netsh int tcp set global ecncapability=enabled')
    run_command('netsh interface ipv4 set subinterface "Ethernet" mtu=1500 store=persistent')
    run_command('netsh int ipv4 set dynamicportrange protocol=tcp start=1025 num=64511')
    run_command('netsh Int ipv4 set glob defaultcurhoplimit=255')
    run_command('netsh Int tcp set global maxsynretransmissions=2')
    run_command('netsh int tcp set global initialRto=2000')
    run_command('netsh int tcp set global rss=disabled')
    run_command('netsh int tcp set global initialwindowsize=65535')
    run_command('netsh int tcp set global numack=2')
    run_command('netsh int tcp set global ackdelay=0')
    run_command('netsh int tcp set global autotuninglevel=normal')
    run_command('netsh int tcp set global congestionprovider=ctcp')
    run_command('netsh int tcp set global ecncapability=disabled')
    run_command('netsh int tcp set global timestamps=disabled')
    run_command('netsh interface teredo set state disabled')
    run_command('netsh int teredo set state disabled')
    run_command('netsh winsock reset')
    registry_commands = [
        f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces" /v "DisableTaskOffload" /t REG_DWORD /d "{dto_value}" /f',
        f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "DisableTaskOffload" /t REG_DWORD /d "{dto_value}" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider" /v "LocalPriority" /t REG_DWORD /d "4" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider" /v "HostsPriority" /t REG_DWORD /d "5" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider" /v "DnsPriority" /t REG_DWORD /d "6" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider" /v "NetbtPriority" /t REG_DWORD /d "7" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "DisableDHCPMediaSenseEventLog" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "EnablePMTUBHDetect" /t REG_DWORD /d 0 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "SackOpts" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "SynAttackProtect" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "TcpMaxDupAcks" /t REG_DWORD /d 2 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "TCPNoDelay" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "TcpDelAckTicks" /t REG_DWORD /d 0 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "MaxUserPort" /t REG_DWORD /d 65534 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "TcpWindowSize" /t REG_DWORD /d 65535 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "GlobalMaxTcpWindowSize" /t REG_DWORD /d 65535 /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "EnableNetDMA" /t REG_DWORD /d 0 /f',
    ]
    for cmd in registry_commands:
        run_command(cmd)
    try:
        result = subprocess.run('wmic path win32_networkadapter get GUID | findstr "{"', shell=True, capture_output=True, text=True)
        for guid in result.stdout.strip().split('\n'):
            if guid.strip():
                run_command(f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid.strip()}" /v InterfaceMetric /t REG_DWORD /d 55 /f')
                run_command(f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid.strip()}" /v TCPNoDelay /t REG_DWORD /d 1 /f')
                run_command(f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid.strip()}" /v TcpAckFrequency /t REG_DWORD /d 1 /f')
                run_command(f'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid.strip()}" /v TcpDelAckTicks /t REG_DWORD /d 0 /f')
    except:
        pass
    service_commands = [
        'sc config "Wcmsvc" start=disabled',
        'sc config "NcaSvc" start=demand',
        'sc config "NetSetupSvc" start=demand',
        'sc config "iphlpsvc" start=disabled',
        'sc config "BthAvctpSvc" start=disabled',
        'sc config "BthHFSrv" start=disabled',
        'sc config "BTAGService" start=manual',
        'sc config "bthserv" start=manual',
        'sc config "Netlogon" start=disabled',
        'sc config "Netman" start=disabled',
        'sc config "WwanSvc" start=disabled',
        'sc config "wcncsvc" start=disabled',
        'sc config "Dhcp" start=auto',
        'sc config "Dnscache" start=auto',
        'sc config "NlaSvc" start=auto',
        'sc config "WlanSvc" start=auto',
        'sc config "netprofm" start=demand',
        'sc config "BluetoothUserService" start=demand',
    ]
    for cmd in service_commands:
        run_command(cmd)
    run_command('PowerShell -ExecutionPolicy Unrestricted -Command "reg add \'HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\SSL 2.0\\Server\' /v \'Enabled\' /t \'REG_DWORD\' /d \'0\' /f"')
    run_command('PowerShell -ExecutionPolicy Unrestricted -Command "reg add \'HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\SSL 3.0\\Server\' /v \'Enabled\' /t \'REG_DWORD\' /d \'0\' /f"')
    run_command('PowerShell -ExecutionPolicy Unrestricted -Command "reg add \'HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\TLS 1.0\\Server\' /v \'Enabled\' /t \'REG_DWORD\' /d \'0\' /f"')
    run_command('PowerShell -ExecutionPolicy Unrestricted -Command "reg add \'HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\TLS 1.1\\Server\' /v \'Enabled\' /t \'REG_DWORD\' /d \'0\' /f"')
    run_command('PowerShell -ExecutionPolicy Unrestricted -Command "reg add \'HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\TLS 1.2\\Server\' /v \'Enabled\' /t \'REG_DWORD\' /d \'1\' /f"')
    run_command('PowerShell -ExecutionPolicy Unrestricted -Command "reg add \'HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\TLS 1.3\\Server\' /v \'Enabled\' /t \'REG_DWORD\' /d \'1\' /f"')

def telemetry_diagnostics_optimizations():
    service_commands = [
        'sc config DPS start=Disabled',
        'sc config "UmRdpService" start=disabled',
        'sc config "DPS" start=disabled',
        'sc config "WdiServiceHost" start=disabled',
        'sc config "WdiSystemHost" start=disabled',
        'sc config "PcaSvc" start=disabled',
        'sc config "diagsvc" start=disabled',
        'sc config "SSDPSRV" start=disabled',
        'sc config DiagTrack start=Disabled',
        'sc config dmwappushservice start=Disabled',
        'sc config diagnosticshub.standardcollector.service start=Disabled',
        'sc config WerSvc start=disabled',
    ]
    for cmd in service_commands:
        run_command(cmd)
    run_command('net stop DiagTrack')
    run_command('net stop dmwappushservice')
    run_command('net stop diagnosticshub.standardcollector.service')
    run_command('net stop WerSvc')
    registry_commands = [
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\Autologger\\AppModel" /v "Start" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\Autologger\\Cellcore" /v "Start" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\Autologger\\Circular Kernel Context Logger" /v "Start" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\Autologger\\CloudExperienceHostOobe" /v "Start" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\Autologger\\DataMarket" /v "Start" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\Autologger\\DiagLog" /v "Start" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v "DoNotShowFeedbackNotifications" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v "AllowCommercialDataPipeline" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v "AllowDeviceNameInTelemetry" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AdvertisingInfo" /v "DisabledByGroupPolicy" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" /v "Enabled" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" /v "Enabled" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Error Reporting" /v "DoReport" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Error Reporting" /v "LoggingDisabled" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Error Reporting" /v "Disabled" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKCU\\Software\\Microsoft\\Office\\Common\\ClientTelemetry" /v "DisableTelemetry" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKCU\\Software\\Microsoft\\Office\\16.0\\Common" /v "sendcustomerdata" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKCU\\Software\\Microsoft\\Office\\16.0\\Common\\Feedback" /v "Enabled" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Edge" /v "SendSiteInfoToImproveServices" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Edge" /v "MetricsReportingEnabled" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Edge" /v "ConfigureDoNotTrack" /t REG_DWORD /d "1" /f',
    ]
    for cmd in registry_commands:
        run_command(cmd)
    scheduled_tasks = [
        'schtasks /change /tn "\\Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\Application Experience\\ProgramDataUpdater" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\Application Experience\\AitAgent" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\Customer Experience Improvement Program\\BthSQM" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\Customer Experience Improvement Program\\KernelCeipTask" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticResolver" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\Feedback\\Siuf\\DmClient" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\Feedback\\Siuf\\DmClientOnScenarioDownload" /Disable',
        'schtasks /change /tn "\\Microsoft\\Windows\\Windows Error Reporting\\QueueReporting" /Disable',
    ]
    for cmd in scheduled_tasks:
        run_command(cmd)
    run_command('Reg.exe add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Search" /v "BingSearchEnabled" /t REG_DWORD /d "0" /f')
    run_command('Reg.exe add "HKLM\\Software\\Policies\\Microsoft\\Windows\\Windows Search" /v "AllowCortana" /t REG_DWORD /d "0" /f')
    run_command('Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" /v "DisableWebSearch" /t REG_DWORD /d "1" /f')

def misc_optimizations():
    registry_commands = [
        'Reg.exe add "HKCU\\Control Panel\\Accessibility\\Keyboard Response" /v "Flags" /t REG_SZ /d "122" /f',
        'Reg.exe add "HKCU\\Control Panel\\Accessibility\\ToggleKeys" /v "Flags" /t REG_SZ /d "58" /f',
        'Reg.exe add "HKCU\\Control Panel\\Accessibility\\StickyKeys" /v "Flags" /t REG_SZ /d "506" /f',
        'Reg.exe add "HKCU\\Control Panel\\Mouse" /v "MouseSpeed" /t REG_SZ /d "0" /f',
        'Reg.exe add "HKCU\\Control Panel\\Mouse" /v "MouseThreshold1" /t REG_SZ /d "0" /f',
        'Reg.exe add "HKCU\\Control Panel\\Mouse" /v "MouseThreshold2" /t REG_SZ /d "0" /f',
        'Reg.exe add "HKCU\\Control Panel\\Mouse" /v "MouseSensitivity" /t REG_SZ /d "10" /f',
        'Reg.exe add "HKCU\\Control Panel\\Keyboard" /v "KeyboardDelay" /t REG_SZ /d "0" /f',
        'Reg.exe add "HKCU\\Control Panel\\Keyboard" /v "KeyboardSpeed" /t REG_SZ /d "31" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\bam" /v "Start" /t REG_DWORD /d "4" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\dam" /v "Start" /t REG_DWORD /d "4" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "Latency" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "HighestPerformance" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v "MaximumPerformancePercent" /t REG_DWORD /d "100" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\kbdclass\\Parameters" /v "KeyboardDataQueueSize" /t REG_DWORD /d "50" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\mouclass\\Parameters" /v "MouseDataQueueSize" /t REG_DWORD /d "50" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\OneDrive" /v "DisableFileSyncNGSC" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\OneDrive" /v "DisableFileSync" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SysMain" /v "Start" /t REG_DWORD /d "4" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\WSearch" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\DoSvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\UsoSvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\wuauserv" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\WaaSMedicSvc" /v "Start" /t REG_DWORD /d "4" /f',
        'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\BITS" /v "Start" /t REG_DWORD /d "4" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "RMDeepL1EntryLatencyUsec" /t REG_DWORD /d "1" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "EnableUlps" /t REG_DWORD /d "0" /f',
        'Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "PP_ThermalAutoThrottlingEnable" /t REG_DWORD /d "0" /f',
    ]
    for cmd in registry_commands:
        run_command(cmd)
    run_command('PowerShell -Command "Get-AppxPackage *Getstarted* | Remove-AppxPackage"')
    run_command('PowerShell -Command "Get-AppxPackage *bing* | Remove-AppxPackage"')
    run_command('PowerShell -Command "Get-AppxPackage *xbox* | Remove-AppxPackage"')
    run_command('PowerShell -Command "Get-AppxPackage *Solitaire* | Remove-AppxPackage"')
    scheduled_tasks = [
        'schtasks /Change /TN "\\Microsoft\\Windows\\Defrag\\ScheduledDefrag" /Disable',
        'schtasks /Change /TN "\\Microsoft\\Windows\\Maintenance\\WinSAT" /Disable',
        'schtasks /Change /TN "\\Microsoft\\Windows\\UpdateOrchestrator\\Schedule Scan" /Disable',
        'schtasks /Change /TN "\\Microsoft\\Windows\\WindowsUpdate\\Scheduled Start" /Disable',
    ]
    for cmd in scheduled_tasks:
        run_command(cmd)

def main():
    if os.name != 'nt':
        sys.exit(1)
    network_optimizations()
    telemetry_diagnostics_optimizations()
    misc_optimizations()

if __name__ == '__main__':
    main()
