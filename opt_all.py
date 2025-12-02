import subprocess
import winreg as reg
import json
from pathlib import Path

BACKUP_FILE = 'backup_all.json'

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except Exception:
        pass

def set_reg(root_key, path, name, value, value_type):
    try:
        key = reg.CreateKeyEx(root_key, path, 0, reg.KEY_WRITE)
        reg.SetValueEx(key, name, 0, value_type, value)
        reg.CloseKey(key)
    except Exception:
        pass

def get_reg(root_key, path, name):
    try:
        key = reg.OpenKey(root_key, path, 0, reg.KEY_READ)
        value, vtype = reg.QueryValueEx(key, name)
        reg.CloseKey(key)
        return (value, vtype)
    except Exception:
        return (None, None)

def apply_all():
    run_cmd("netsh int teredo set state disabled")
    run_cmd("netsh int tcp set heuristics disabled")
    run_cmd("netsh winsock reset")
    run_cmd("netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent")
    run_cmd("netsh interface tcp set global initialrto=2000")
    run_cmd("netsh advfirewall set allprofiles state off")
    run_cmd("netsh int tcp set global autotuninglevel=disabled")
    run_cmd("netsh int tcp set global rss=disabled")
    run_cmd("netsh int tcp set global chimney=enabled")
    run_cmd("netsh int tcp set global netdma=enabled")
    run_cmd("netsh int tcp set global dca=enabled")
    run_cmd("netsh int tcp set global congestionprovider=ctcp")
    run_cmd("netsh int tcp set global timestamps=disabled")
    run_cmd("netsh int tcp set global fastopen=enabled")
    run_cmd("netsh Int tcp set global nonsackrttresiliency=disabled")
    run_cmd("netsh int tcp set global ecncapability=disabled")
    run_cmd("netsh interface ipv4 set subinterface \"Ethernet\" mtu=1500 store=persistent")
    run_cmd("netsh int ipv4 set dynamicportrange protocol=tcp start=1025 num=64511")
    run_cmd("netsh Int ipv4 set glob defaultcurhoplimit=255")
    run_cmd("netsh Int tcp set global maxsynretransmissions=2")
    run_cmd("netsh int tcp set global initialwindowsize=65535")
    run_cmd("netsh int tcp set global numack=2")
    run_cmd("netsh int tcp set global ackdelay=0")
    
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\" /v \"LocalPriority\" /t REG_DWORD /d \"4\" /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\" /v \"HostsPriority\" /t REG_DWORD /d \"5\" /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\" /v \"DnsPriority\" /t REG_DWORD /d \"6\" /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\" /v \"NetbtPriority\" /t REG_DWORD /d \"7\" /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"DisableDHCPMediaSenseEventLog\" /t REG_DWORD /d 1 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"EnablePMTUBHDetect\" /t REG_DWORD /d 0 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"SackOpts\" /t REG_DWORD /d 1 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"SynAttackProtect\" /t REG_DWORD /d 1 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpMaxDupAcks\" /t REG_DWORD /d 2 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpAckFrequency\" /t REG_DWORD /d 1 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TCPNoDelay\" /t REG_DWORD /d 1 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpDelAckTicks\" /t REG_DWORD /d 0 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"MaxUserPort\" /t REG_DWORD /d 65534 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"TcpWindowSize\" /t REG_DWORD /d 65535 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"GlobalMaxTcpWindowSize\" /t REG_DWORD /d 65535 /f")
    run_cmd("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" /v \"EnableNetDMA\" /t REG_DWORD /d 0 /f")

def get_backup_data():
    backup = {'marker': 'backup_created'}
    return backup

def restore_from_backup(backup_data):
    if not backup_data or 'marker' not in backup_data:
        return
