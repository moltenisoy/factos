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


def apply_net_deep():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'netsh int tcp set global autotuninglevel=normal',
        r'netsh int tcp set global chimney=disabled',
        r'netsh int tcp set global dca=enabled',
        r'netsh int tcp set global netdma=enabled',
        r'netsh int tcp set global ecncapability=disabled',
        r'netsh int tcp set global timestamps=disabled',
        r'netsh int tcp set global rss=enabled',
        r'netsh int tcp set global fastopen=enabled',
        r'netsh int tcp set global fastopenfallback=enabled',
        r'netsh int tcp set global hystart=disabled',
        r'netsh int tcp set global pacingprofile=off',
        r'netsh int tcp set global maxsynretransmissions=2',
        r'netsh int tcp set global nonsackrttresiliency=disabled',
        r'netsh int tcp set global initialRto=2000',
        r'netsh int tcp set global mtu=1500',
        r'netsh int udp set global uro=enabled',
        r'netsh int ip set global taskoffload=enabled',
        r'netsh int ip set global reassemblylimit=33554432',
        r'netsh int ip set global neighborcachelimit=4096',
        r'netsh int ip set global routecachelimit=4096',
        r'netsh int ip set global multicastforwarding=disabled',
        r'netsh int ip set global randomizeidentifiers=disabled',
        r'netsh int ip set global addressmaskreply=disabled',
        r'netsh int ip set global sourceroutingbehavior=drop',
        r'netsh int ipv6 set global randomizeidentifiers=disabled',
        r'netsh int ipv6 set global addressmaskreply=disabled',
        r'netsh int ipv6 set global multicastforwarding=disabled',
        r'netsh int ipv6 set teredo state=disabled',
        r'netsh int ipv6 set isatap state=disabled',
        r'netsh int ipv6 set 6to4 state=disabled',
        r'netsh winsock reset',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TcpAckFrequency /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TCPNoDelay /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TcpDelAckTicks /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TcpMaxDupAcks /t REG_DWORD /d 2 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v GlobalMaxTcpWindowSize /t REG_DWORD /d 65535 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TcpWindowSize /t REG_DWORD /d 65535 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v MaxConnectionsPerServer /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v MaxUserPort /t REG_DWORD /d 65534 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TcpTimedWaitDelay /t REG_DWORD /d 30 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v DefaultTTL /t REG_DWORD /d 64 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v SackOpts /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v Tcp1323Opts /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v EnablePMTUDiscovery /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v EnablePMTUBHDetect /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v KeepAliveInterval /t REG_DWORD /d 1000 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v KeepAliveTime /t REG_DWORD /d 300000 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v DisableTaskOffload /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v EnableICMPRedirect /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v DeadGWDetectDefault /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v DontAddDefaultGatewayDefault /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters" /v DisabledComponents /t REG_DWORD /d 32 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v IRPStackSize /t REG_DWORD /d 20 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v SizReqBuf /t REG_DWORD /d 17424 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v MaxMpxCt /t REG_DWORD /d 1024 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v MaxWorkItems /t REG_DWORD /d 1024 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v MaxCmds /t REG_DWORD /d 1024 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v EnableOplocks /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v Lmannounce /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\QoS" /v Tcp_1323_Opts /t REG_SZ /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\AFD\Parameters" /v DefaultSendWindow /t REG_DWORD /d 131072 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\AFD\Parameters" /v DefaultReceiveWindow /t REG_DWORD /d 131072 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\AFD\Parameters" /v FastSendDatagramThreshold /t REG_DWORD /d 1024 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\AFD\Parameters" /v IgnorePushBitOnReceives /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\AFD\Parameters" /v NonBlockingSendSpecialBuffering /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\AFD\Parameters" /v DynamicSendBufferDisable /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" /v CacheHashTableBucketSize /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" /v CacheHashTableSize /t REG_DWORD /d 384 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" /v MaxCacheEntryTtlLimit /t REG_DWORD /d 86400 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" /v MaxSOACacheEntryTtlLimit /t REG_DWORD /d 300 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" /v NegativeCacheTime /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" /v NegativeSOACacheTime /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" /v NetFailureCacheTime /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Psched" /v NonBestEffortLimit /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\NDIS\Parameters" /v MaxInterruptModeration /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\NDIS\Parameters" /v MinInterruptModeration /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\NDIS\Parameters" /v EnableCoalescing /t REG_DWORD /d 0 /f',
        r'netsh int tcp set supplemental template=internet congestionprovider=ctcp',
        r'netsh interface tcp set heuristics disabled',
    ]

    for cmd in commands:
        run(cmd)


if __name__ == "__main__":
    apply_net_deep()
