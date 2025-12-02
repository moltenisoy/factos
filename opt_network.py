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


def apply_network():
    """Optimizaciones de red: TCP/IP, DNS, firewall y configuraciones de red"""
    if os.name != "nt":
        sys.exit(1)

    # TCP/IP optimizations
    run("netsh int teredo set state disabled")
    run("netsh int tcp set heuristics Disabled")
    run("netsh winsock reset")
    run("netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent")
    run("netsh interface tcp set global initialrto=2000")
    run("netsh advfirewall set allprofiles state off")
    run("netsh int tcp set global autotuninglevel=normal")
    run("netsh int tcp set global rss=enabled")
    run("netsh int tcp set global chimney=enabled")
    run("netsh int tcp set global netdma=enabled")
    run("netsh int tcp set global dca=enabled")
    run("netsh int tcp set global congestionprovider=ctcp")
    run("netsh int tcp set heuristics disabled")
    run("netsh int tcp set global timestamps=disabled")
    run("netsh int tcp set global fastopen=enabled")
    run("netsh Int tcp set global nonsackrttresiliency=disabled")
    run("netsh int tcp set global autotuninglevel=disabled")
    run("netsh int tcp set global ecncapability=enabled")
    run("netsh interface ipv4 set subinterface \"Ethernet\" mtu=1500 store=persistent")
    run("netsh int ipv4 set dynamicportrange protocol=tcp start=1025 num=64511")
    run("netsh Int ipv4 set glob defaultcurhoplimit=255")
    run("netsh Int tcp set global maxsynretransmissions=2")
    run("netsh int tcp set global initialRto=2000")
    run("netsh int tcp set global rss=disabled")
    run("netsh int tcp set global initialwindowsize=65535")
    run("netsh int tcp set global numack=2")
    run("netsh int tcp set global ackdelay=0")
    run("netsh int tcp set global ecncapability=disabled")
    run("netsh interface teredo set state disabled")

    # Registry TCP/IP settings
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\" /v \"LocalPriority\" /t REG_DWORD /d \"4\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\" /v \"HostsPriority\" /t REG_DWORD /d \"5\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\" /v \"DnsPriority\" /t REG_DWORD /d \"6\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\" /v \"NetbtPriority\" /t REG_DWORD /d \"7\" /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"DisableDHCPMediaSenseEventLog\" /t REG_DWORD /d 1 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"EnablePMTUBHDetect\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"SackOpts\" /t REG_DWORD /d 1 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"SynAttackProtect\" /t REG_DWORD /d 1 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpMaxDupAcks\" /t REG_DWORD /d 2 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpAckFrequency\" /t REG_DWORD /d 1 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TCPNoDelay\" /t REG_DWORD /d 1 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpDelAckTicks\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"MaxUserPort\" /t REG_DWORD /d 65534 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpWindowSize\" /t REG_DWORD /d 65535 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"GlobalMaxTcpWindowSize\" /t REG_DWORD /d 65535 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"EnableNetDMA\" /t REG_DWORD /d 0 /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"MaxConnectionsPer1_0Server\" /t REG_DWORD /d \"16\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"MaxConnectionsPerServer\" /t REG_DWORD /d \"16\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"EnableConnectionRateLimiting\" /t REG_DWORD /d \"00000000\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"EnableRSS\" /t REG_DWORD /d \"00000001\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"EnableTCPA\" /t REG_DWORD /d \"00000001\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"EnableWsd\" /t REG_DWORD /d \"00000000\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"MaxFreeTcbs\" /t REG_DWORD /d \"65535\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"MaxHashTableSize\" /t REG_DWORD /d \"00010000\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"Tcp1323Opts\" /t REG_DWORD /d \"00000001\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpMaxDataRetransmissions\" /t REG_DWORD /d \"4\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"StrictTimeWaitSeqCheck\" /t REG_DWORD /d \"00000001\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"DisableIPSourceRouting\" /t REG_DWORD /d \"00000008\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpCreateAndConnectTcbRateLimitDepth\" /t REG_DWORD /d \"00000000\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"IPAutoconfigurationEnabled\" /t REG_DWORD /d \"00000000\" /f")
    run("Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"DefaultTTL\" /t REG_DWORD /d \"38\" /f")

    # Network adapter optimizations
    run("Reg.exe add \"%%n\" /v \"AdvancedEEE\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"*EEE\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"EEE\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"EEELinkAdvertisement\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"EnableWakeOnLan\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"S5WakeOnLan\" /t REG_SZ /d \"0\" /f")
    run("Reg.exe add \"%%n\" /v \"JumboPacket\" /t REG_SZ /d \"1514\" /f")
    run("Reg.exe add \"%%n\" /v \"TransmitBuffers\" /t REG_SZ /d \"2048\" /f")
    run("Reg.exe add \"%%n\" /v \"ReceiveBuffers\" /t REG_SZ /d \"1024\" /f")

    # Network services
    run("sc config \"Wcmsvc\" start=disabled")
    run("sc config \"NcaSvc\" start=demand")
    run("sc config \"NetSetupSvc\" start=demand")
    run("sc config \"iphlpsvc\" start=disabled")
    run("sc config \"Netlogon\" start=disabled")
    run("sc config \"Netman\" start=disabled")
    run("sc config \"WwanSvc\" start=disabled")
    run("sc config \"wcncsvc\" start=disabled")
    run("sc config \"Dhcp\" start=auto")
    run("sc config \"Dnscache\" start=auto")
    run("sc config \"NlaSvc\" start=auto")
    run("sc config \"WlanSvc\" start=auto")
    run("sc config \"netprofm\" start=demand")
