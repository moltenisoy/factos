import subprocess
import winreg as reg

def apply():
    commands = [
        'netsh int teredo set state disabled',
        'netsh int tcp set heuristics Disabled',
        'netsh winsock reset',
        'netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent',
        'netsh interface tcp set global initialrto=2000',
        'netsh int tcp set global autotuninglevel=normal',
        'netsh int tcp set global rss=enabled',
        'netsh int tcp set global chimney=enabled',
        'netsh int tcp set global netdma=enabled',
        'netsh int tcp set global dca=enabled',
        'netsh int tcp set global congestionprovider=ctcp',
        'netsh int tcp set heuristics disabled',
        'netsh int tcp set global timestamps=disabled',
        'netsh int tcp set global fastopen=enabled',
        'netsh Int tcp set global nonsackrttresiliency=disabled',
        'netsh int tcp set global autotuninglevel=disabled',
        'netsh int tcp set global ecncapability=enabled',
        'netsh interface ipv4 set subinterface "Ethernet" mtu=1500 store=persistent',
        'netsh int ipv4 set dynamicportrange protocol=tcp start=1025 num=64511',
        'netsh Int ipv4 set glob defaultcurhoplimit=255',
        'netsh Int tcp set global maxsynretransmissions=2',
        'netsh int tcp set global initialRto=2000',
        'netsh int tcp set global rss=disabled',
        'netsh int tcp set global initialwindowsize=65535',
        'netsh int tcp set global numack=2',
        'netsh int tcp set global ackdelay=0',
        'netsh int tcp set global ecncapability=disabled',
        'netsh interface teredo set state disabled',
    ]
    for cmd in commands:
        try:
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
    
    registry_entries = [
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider', 'LocalPriority', 4, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider', 'HostsPriority', 5, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider', 'DnsPriority', 6, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider', 'NetbtPriority', 7, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'DisableDHCPMediaSenseEventLog', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'EnablePMTUBHDetect', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'SackOpts', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'SynAttackProtect', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'TcpMaxDupAcks', 2, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'TcpAckFrequency', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'TCPNoDelay', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'TcpDelAckTicks', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'MaxUserPort', 65534, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'TcpWindowSize', 65535, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'GlobalMaxTcpWindowSize', 65535, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'EnableNetDMA', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'MaxConnectionsPer1_0Server', 16, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'MaxConnectionsPerServer', 16, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'DefaultTTL', 56, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Dnscache\Parameters', 'CacheHashTableBucketSize', 1, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Dnscache\Parameters', 'CacheHashTableSize', 384, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Dnscache\Parameters', 'NegativeCacheTime', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Dnscache\Parameters', 'NetFailureCacheTime', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Dnscache\Parameters', 'NegativeSOACacheTime', 0, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\AFD\Parameters', 'FastCopyReceiveThreshold', 2048, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\AFD\Parameters', 'FastSendDatagramThreshold', 2048, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\AFD\Parameters', 'DefaultSendWindow', 415029, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\AFD\Parameters', 'DefaultReceiveWindow', 415029, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\AFD\Parameters', 'MaxFastCopyTransmit', 296, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\AFD\Parameters', 'MaxFastTransmit', 100, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\AFD\Parameters', 'TransmitWorker', 50, reg.REG_DWORD),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters', 'DisabledComponents', 255, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\Psched', 'NonBestEffortLimit', 0, reg.REG_DWORD),
        (r'SOFTWARE\Policies\Microsoft\Windows\Psched', 'TimerResolution', 1, reg.REG_DWORD),
    ]
    
    for path, name, value, vtype in registry_entries:
        try:
            key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
            reg.SetValueEx(key, name, 0, vtype, value)
            reg.CloseKey(key)
        except:
            pass

    services = [
        ('Wcmsvc', 'disabled'),
        ('NcaSvc', 'demand'),
        ('NetSetupSvc', 'demand'),
        ('iphlpsvc', 'disabled'),
        ('Dhcp', 'auto'),
        ('Dnscache', 'auto'),
        ('NlaSvc', 'auto'),
        ('WlanSvc', 'auto'),
    ]
    
    for service, start_type in services:
        try:
            subprocess.run(f'sc config "{service}" start={start_type}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

def get_backup_data():
    backup = {}
    backup['registry'] = []
    
    registry_paths = [
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider', ['LocalPriority', 'HostsPriority', 'DnsPriority', 'NetbtPriority']),
        (r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', ['TcpAckFrequency', 'TCPNoDelay', 'TcpDelAckTicks', 'MaxUserPort', 'TcpWindowSize', 'GlobalMaxTcpWindowSize']),
        (r'SYSTEM\CurrentControlSet\Services\Dnscache\Parameters', ['CacheHashTableBucketSize', 'CacheHashTableSize', 'NegativeCacheTime']),
        (r'SYSTEM\CurrentControlSet\Services\AFD\Parameters', ['DefaultSendWindow', 'DefaultReceiveWindow']),
    ]
    
    for path, value_names in registry_paths:
        try:
            key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_READ)
            for name in value_names:
                try:
                    value, vtype = reg.QueryValueEx(key, name)
                    backup['registry'].append((path, name, value, vtype))
                except:
                    backup['registry'].append((path, name, None, None))
            reg.CloseKey(key)
        except:
            pass
    
    return backup

def restore(backup_data):
    if not backup_data:
        return
    
    for path, name, value, vtype in backup_data.get('registry', []):
        try:
            if value is not None:
                key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
                reg.SetValueEx(key, name, 0, vtype, value)
                reg.CloseKey(key)
            else:
                try:
                    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_WRITE)
                    reg.DeleteValue(key, name)
                    reg.CloseKey(key)
                except:
                    pass
        except:
            pass
