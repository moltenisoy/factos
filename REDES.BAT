@echo off
setlocal EnableExtensions DisableDelayedExpansion

REM =========================================================
REM === DETECCION INTELIGENTE DE NUCLEOS DE CPU ===
REM =========================================================
set "CPU_CORES=0"
for /f "tokens=2 delims==" %%A in ('wmic cpu get NumberOfCores /value ^| find "="') do set /a CPU_CORES=%%A

echo Nucleos detectados: %CPU_CORES%

IF %CPU_CORES% GEQ 6 (
    REM === CASO: 6 O MAS NUCLEOS (CARGA AL PROCESADOR) ===
    echo CPU Robusto detectado. Optimizando para MENOR LATENCIA (Cargando proceso al CPU)...
    REM Netsh: Desactivar descarga a la NIC
    set "_N_TO=Disabled"
    REM Registro: DisableTaskOffload = 1 (Verdadero, desactivar offload)
    set "_R_DTO=1"
    REM Registro NIC: Poner en 0 las capacidades de la tarjeta para forzar al CPU
    set "_R_NIC=0"
) ELSE (
    REM === CASO: MENOS DE 6 NUCLEOS (CARGA A LA RED) ===
    echo CPU Limitado detectado. Optimizando para RENDIMIENTO (Descargando proceso a la Placa de Red)...
    REM Netsh: Activar descarga a la NIC
    set "_N_TO=Enabled"
    REM Registro: DisableTaskOffload = 0 (Falso, permitir offload)
    set "_R_DTO=0"
    REM Registro NIC: Poner en 1 (o 3) las capacidades para que la tarjeta trabaje
    set "_R_NIC=1"
)
REM =========================================================

REM === CONFIGURACION NETSH ===
netsh int teredo set state disabled
netsh int tcp set heuristics Disabled
netsh int ip set global taskoffload=%_N_TO%
netsh winsock reset
netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent >nul 2>&1
netsh interface tcp set global initialrto=2000 >nul 2>&1
netsh advfirewall set allprofiles state off >nul 2>&1
netsh int tcp set global autotuninglevel=normal >nul 2>&1
netsh int tcp set global rss=enabled >nul 2>&1
netsh int tcp set global chimney=enabled >nul 2>&1
netsh int tcp set global netdma=enabled >nul 2>&1
netsh int tcp set global dca=enabled >nul 2>&1
netsh int tcp set global congestionprovider=ctcp >nul 2>&1
netsh int tcp set heuristics disabled >nul 2>&1 
netsh int tcp set global timestamps=disabled >nul 2>&1 
netsh int tcp set global fastopen=enabled >nul 2>&1 
netsh Int tcp set global nonsackrttresiliency=disabled >nul 2>&1 
netsh Int tcp set global netdma=enabled >nul 2>&1 
netsh Int tcp set global congestionprovider=ctcp >nul 2>&1 
netsh Int tcp set global dca=enabled >nul 2>&1 
netsh int tcp set global autotuninglevel=disabled >nul 2>&1 
netsh int tcp set global ecncapability=enabled >nul 2>&1 
netsh interface ipv4 set subinterface "Ethernet" mtu=1500 store=persistent >nul 2>&1 
netsh int ipv4 set dynamicportrange protocol=tcp start=1025 num=64511 >nul 2>&1 
netsh Int ipv4 set glob defaultcurhoplimit=255 >nul 2>&1 
netsh Int tcp set global maxsynretransmissions=2 >nul 2>&1 
netsh int tcp set global initialRto=2000 >nul 2>&1 
netsh int tcp set global rss=disabled >nul 2>&1 
netsh int tcp set global initialwindowsize=65535 >nul 2>&1 
netsh int tcp set global numack=2 >nul 2>&1 
netsh int tcp set global ackdelay=0 >nul 2>&1 
netsh int tcp set global autotuninglevel=normal  >nul 2>&1 
netsh int tcp set global congestionprovider=ctcp  >nul 2>&1 
netsh int tcp set global ecncapability=disabled  >nul 2>&1 
netsh int tcp set global timestamps=disabled  >nul 2>&1 
netsh interface teredo set state disabled  >nul 2>&1 
netsh int teredo set state disabled >nul 2>&1 
netsh winsock reset >nul 2>&1 

REM === PARAMETROS TCPIP ===
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "DisableTaskOffload" /t REG_DWORD /d "%_R_DTO%" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "DisableTaskOffload" /t REG_DWORD /d "%_R_DTO%" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "LocalPriority" /t REG_DWORD /d "4" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "HostsPriority" /t REG_DWORD /d "5" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "DnsPriority" /t REG_DWORD /d "6" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "NetbtPriority" /t REG_DWORD /d "7" /f
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%%q" /v InterfaceMetric /t REG_DWORD /d 55 /f 
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%%q" /v TCPNoDelay /t REG_DWORD /d 1 /f 
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%%q" /v TcpAckFrequency /t REG_DWORD /d 1 /f 
    Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%%q" /v TcpDelAckTicks /t REG_DWORD /d 0 /f 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "DisableDHCPMediaSenseEventLog" /t REG_DWORD /d 1 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnablePMTUBHDetect" /t REG_DWORD /d 0 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "SackOpts" /t REG_DWORD /d 1 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "SynAttackProtect" /t REG_DWORD /d 1 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpMaxDupAcks" /t REG_DWORD /d 2 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TCPNoDelay" /t REG_DWORD /d 1 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpDelAckTicks" /t REG_DWORD /d 0 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "MaxUserPort" /t REG_DWORD /d 65534 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpWindowSize" /t REG_DWORD /d 65535 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "GlobalMaxTcpWindowSize" /t REG_DWORD /d 65535 /f >nul
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnableNetDMA" /t REG_DWORD /d 0 /f >nul
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "MaxConnectionsPer1_0Server" /t REG_DWORD /d "16" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "MaxConnectionsPerServer" /t REG_DWORD /d "16" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "DisableTaskOffload" /t REG_DWORD /d "%_R_DTO%" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnableConnectionRateLimiting" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnablePMTUBHDetect" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnablePMTUDiscovery" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnableRSS" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnableTCPA" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnableWsd" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "MaxFreeTcbs" /t REG_DWORD /d "65535" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "MaxHashTableSize" /t REG_DWORD /d "00010000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "MaxUserPort" /t REG_DWORD /d "65534" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "SackOpts" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "SizReqBuf" /t REG_DWORD /d "51319" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "SynAttackProtect" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TCPNoDelay" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "Tcp1323Opts" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpMaxDataRetransmissions" /t REG_DWORD /d "4" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpAckFrequency" /t REG_DWORD /d "00000005" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "StrictTimeWaitSeqCheck" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "DisableIPSourceRouting" /t REG_DWORD /d "00000008" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpCreateAndConnectTcbRateLimitDepth" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TCPInitalRtt" /t REG_DWORD /d "00046325" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpMaxDupAcks" /t REG_DWORD /d "00000002" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TCPDelAckTicks" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "IPAutoconfigurationEnabled" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "DefaultTTL" /t REG_DWORD /d "38" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "DisableTaskOffload" /t REG_DWORD /d "%_R_DTO%" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "EnableConnectionRateLimiting" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "EnableDCA" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "EnablePMTUBHDetect" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "EnablePMTUDiscovery" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "EnableRSS" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "EnableTCPA" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "EnableWsd" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "MaxFreeTcbs" /t REG_DWORD /d "65535" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "MaxHashTableSize" /t REG_DWORD /d "00010000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "MaxUserPort" /t REG_DWORD /d "65534" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "SackOpts" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "SizReqBuf" /t REG_DWORD /d "51319" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "SynAttackProtect" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TCPNoDelay" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "Tcp1323Opts" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TcpMaxDataRetransmissions" /t REG_DWORD /d "5" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TcpAckFrequency" /t REG_DWORD /d "00000004" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "StrictTimeWaitSeqCheck" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "DisableIPSourceRouting" /t REG_DWORD /d "00000008" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TcpCreateAndConnectTcbRateLimitDepth" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "IPAutoconfigurationEnabled" /t REG_DWORD /d "00000000" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TCPInitalRtt" /t REG_DWORD /d "00046325" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TcpMaxDupAcks" /t REG_DWORD /d "00000002" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TCPDelAckTicks" /t REG_DWORD /d "00000001" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "DefaultTTL" /t REG_DWORD /d "38" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "LocalPriority" /t REG_DWORD /d "239" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "HostsPriority" /t REG_DWORD /d "240" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "DnsPriority" /t REG_DWORD /d "1740" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "NetbtPriority" /t REG_DWORD /d "1741" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "LocalPriority" /t REG_DWORD /d "4" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "HostsPriority" /t REG_DWORD /d "5" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "DnsPriority" /t REG_DWORD /d "6" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" /v "NetbtPriority" /t REG_DWORD /d "7" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Winsock" /v "UseDelayedAcceptance" /t REG_DWORD /d "0" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Winsock" /v "MaxSockAddrLength" /t REG_DWORD /d "16" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Winsock" /v "MinSockAddrLength" /t REG_DWORD /d "16" /f >nul 2>&1 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "DisableDHCPMediaSenseEventLog" /t REG_DWORD /d 1 /f >nul 2>&1 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnablePMTUBHDetect" /t REG_DWORD /d 0 /f >nul 2>&1 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "SackOpts" /t REG_DWORD /d 1 /f >nul 2>&1 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "SynAttackProtect" /t REG_DWORD /d 1 /f >nul 2>&1 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpMaxDupAcks" /t REG_DWORD /d 2 /f >nul 2>&1 
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f >nul 2>&1 
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TCPNoDelay" /t REG_DWORD /d 1 /f >nul 2>&1 
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpDelAckTicks" /t REG_DWORD /d 0 /f >nul 2>&1 
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "MaxUserPort" /t REG_DWORD /d 65534 /f >nul 2>&1 
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpWindowSize" /t REG_DWORD /d 65535 /f >nul 2>&1 
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "GlobalMaxTcpWindowSize" /t REG_DWORD /d 65535 /f >nul 2>&1 
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TcpAckFrequency" /t REG_DWORD /d 1 /f >nul 2>&1 
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "TCPNoDelay" /t REG_DWORD /d 1 /f >nul 2>&1 
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "EnableNetDMA" /t REG_DWORD /d 0 /f >nul 2>&1 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpAckFrequency" /t REG_DWORD /d "1" /f  >nul 2>&1 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TCPNoDelay" /t REG_DWORD /d "1" /f  >nul 2>&1 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "TcpDelAckTicks" /t REG_DWORD /d "0" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" /v "DisableTaskOffload" /t REG_DWORD /d "%_R_DTO%" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "DisablegTaskOffload" /t REG_DWORD /d "%_R_DTO%" /f >nul 2>&1 
for /f %%q in ('wmic path win32_networkadapter get GUID 2^>nul ^| findstr "{"') do Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%%q" /v InterfaceMetric /t REG_DWORD /d "55" /f >nul 2>&1 
for /f %%q in ('wmic path win32_networkadapter get GUID ^| findstr "{"') do Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%%q" /v TCPNoDelay /t REG_DWORD /d "1" /f 
for /f %%q in ('wmic path win32_networkadapter get GUID ^| findstr "{"') do Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%%q" /v TcpAckFrequency /t REG_DWORD /d "1" /f 
for /f %%q in ('wmic path win32_networkadapter get GUID ^| findstr "{"') do Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%%q" /v TcpDelAckTicks /t REG_DWORD /d "0" /f 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "DisableTaskOffload" /t REG_DWORD /d "%_R_DTO%" /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%q" /v InterfaceMetric /t REG_DWORD /d 55 /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%q" /v TCPNoDelay /t REG_DWORD /d 1 /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%q" /v TcpAckFrequency /t REG_DWORD /d 1 /f >nul 2>&1 
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\%q" /v TcpDelAckTicks /t REG_DWORD /d 0 /f >nul 2>&1 

REM === ADAPTADORES DE RED ===
for /f %%i in ('wmic path win32_NetworkAdapter get PNPDeviceID ^| findstr /L "PCI\VEN_"') do (
    Reg.exe add "%%n" /v "AdvancedEEE" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "*EEE" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "EEE" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "EEELinkAdvertisement" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "AutoPowerSaveModeEnabled" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "NicAutoPowerSaver" /t REG_SZ /d "2" /f
    Reg.exe add "%%n" /v "EnableWakeOnLan" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "S5WakeOnLan" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "JumboPacket" /t REG_SZ /d "1514" /f 
    Reg.exe add "%%n" /v "TransmitBuffers" /t REG_SZ /d "2048" /f 
    Reg.exe add "%%n" /v "ReceiveBuffers" /t REG_SZ /d "1024" /f 
    Reg.exe add "%%n" /v "IPChecksumOffloadIPv4" /t REG_SZ /d "%_R_NIC%" /f 
    Reg.exe add "%%n" /v "PMARPOffload" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "PMNSOffload" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "TCPChecksumOffloadIPv4" /t REG_SZ /d "%_R_NIC%" /f 
    Reg.exe add "%%n" /v "TCPChecksumOffloadIPv6" /t REG_SZ /d "%_R_NIC%" /f 
    Reg.exe add "%%n" /v "UDPChecksumOffloadIPv6" /t REG_SZ /d "%_R_NIC%" /f 
    Reg.exe add "%%n" /v "UDPChecksumOffloadIPv4" /t REG_SZ /d "%_R_NIC%" /f 
    Reg.exe add "%%n" /v "RSS" /t REG_SZ /d "1" /f 
    Reg.exe add "%%n" /v "*NumRssQueues" /t REG_SZ /d "2" /f 
    Reg.exe add "%%n" /v "RSSProfile" /t REG_SZ /d "3" /f 
    Reg.exe add "%%n" /v "*FlowControl" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "FlowControlCap" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "FatChannelIntolerant" /t REG_SZ /d "0" /f 
for /f %%q in ('wmic path win32_networkadapter get GUID ^| findstr "{"') do (
sc config "workfolderssvc" start=disabled >nul
powershell -NoProfile -ExecutionPolicy Bypass -Command "& { Get-NetAdapter | Enable-NetAdapterRss -ErrorAction SilentlyContinue; Get-NetAdapter | ForEach-Object { try { Set-NetAdapterAdvancedProperty -Name $_.Name -DisplayName 'Receive Buffers' -RegistryValue 512 -ErrorAction SilentlyContinue } catch {}; try { Set-NetAdapterAdvancedProperty -Name $_.Name -DisplayName 'Transmit Buffers' -RegistryValue 512 -ErrorAction SilentlyContinue } catch {}; try { Set-NetAdapterAdvancedProperty -Name $_.Name -DisplayName 'Energy Efficient Ethernet' -RegistryValue '0' -ErrorAction SilentlyContinue } catch {}; try { Set-NetAdapterAdvancedProperty -Name $_.Name -DisplayName 'Interrupt Moderation' -RegistryValue 'Disabled' -ErrorAction SilentlyContinue } catch {}; try { Set-NetAdapterAdvancedProperty -Name $_.Name -DisplayName 'Flow Control' -RegistryValue 'Disabled' -ErrorAction SilentlyContinue } catch {} } }" >nul 2>&1
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-NetAdapter | Disable-NetAdapterPowerManagement -WakeOnMagicPacket:$false -WakeOnPattern:$false -DeviceSleepOnDisconnect:$false -SelectiveSuspend:$false -ArpOffload:$false -NSOffload:$false -D0PacketCoalescing:$false -RsnRekeyOffload:$false -NoRestart -ErrorAction SilentlyContinue" >nul 2>&1
Reg.exe add "HKLM\SOFTWARE\Policies\Google\Chrome" /v "DefaultSensorsSetting" /t REG_DWORD /d "2" /f >nul 2>&1 
REG DELETE "HKEY_CLASSES_ROOT\CLSID\{a6e02196-c1bf-4989-8a94-144eee4a9bb2}" /f >nul 2>&1 
REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\{a6e02196-c1bf-4989-8a94-144eee4a9bb2}" /f >nul 2>&1 
Reg.exe add "%%n" /v "AdvancedEEE" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "*EEE" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "EEE" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "EEELinkAdvertisement" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "AutoPowerSaveModeEnabled" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "NicAutoPowerSaver" /t REG_SZ /d "2" /f >nul 2>&1 
Reg.exe add "%%n" /v "EnableWakeOnLan" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "S5WakeOnLan" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "JumboPacket" /t REG_SZ /d "1514" /f >nul 2>&1 
Reg.exe add "%%n" /v "TransmitBuffers" /t REG_SZ /d "2048" /f >nul 2>&1 
Reg.exe add "%%n" /v "ReceiveBuffers" /t REG_SZ /d "1024" /f >nul 2>&1 
Reg.exe add "%%n" /v "IPChecksumOffloadIPv4" /t REG_SZ /d "%_R_NIC%" /f >nul 2>&1 
Reg.exe add "%%n" /v "PMARPOffload" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "PMNSOffload" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "TCPChecksumOffloadIPv4" /t REG_SZ /d "%_R_NIC%" /f >nul 2>&1 
Reg.exe add "%%n" /v "TCPChecksumOffloadIPv6" /t REG_SZ /d "%_R_NIC%" /f >nul 2>&1 
Reg.exe add "%%n" /v "UDPChecksumOffloadIPv6" /t REG_SZ /d "%_R_NIC%" /f >nul 2>&1 
Reg.exe add "%%n" /v "UDPChecksumOffloadIPv4" /t REG_SZ /d "%_R_NIC%" /f >nul 2>&1 
Reg.exe add "%%n" /v "RSS" /t REG_SZ /d "1" /f >nul 2>&1 
Reg.exe add "%%n" /v "*NumRssQueues" /t REG_SZ /d "2" /f >nul 2>&1 
Reg.exe add "%%n" /v "RSSProfile" /t REG_SZ /d "3" /f >nul 2>&1 
Reg.exe add "%%n" /v "*FlowControl" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "FlowControlCap" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "FatChannelIntolerant" /t REG_SZ /d "0" /f >nul 2>&1 
sc config "workfolderssvc" start=disabled >nul 2>&1 
sc config "workfolderssvc" start=demand >nul 2>&1 
sc config "workfolderssvc" start= demand >nul 2>&1 
sc config workfolderssvc start=disabled >nul 2>&1 
sc stop workfolderssvc >nul 2>&1 
    Reg.exe add "%%n" /v "EnablePME" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "AutoDisablingGigabit" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "EnableGreenEthernet" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "EnableSavePowerNow" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "EnablePowerManagement" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "PowerDownPll" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "PowerSavingMode" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "ReduceSpeedOnPowerDown" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "S5NicKeepOverrideMacAddrV2" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "EnableConnectedPowerGating" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "GigaLite" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "ULPMode" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "WakeOnDisconnect" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "*WakeOnMagicPacket" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "*WakeOnPattern" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "WakeOnLink" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "WolShutdownLinkSpeed" /t REG_SZ /d "2" /f 
    Reg.exe add "%%n" /v "LsoV1IPv4" /t REG_SZ /d "%_R_NIC%" /f  
    Reg.exe add "%%n" /v "LsoV2IPv4" /t REG_SZ /d "%_R_NIC%" /f 
    Reg.exe add "%%n" /v "LsoV2IPv6" /t REG_SZ /d "%_R_NIC%" /f 
    Reg.exe add "%%n" /v "RxAbsIntDelay" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "TxIntDelay" /t REG_SZ /d "0" /f 
    Reg.exe add "%%n" /v "TxAbsIntDelay" /t REG_SZ /d "0" /f 
reg add "HKLM\SYSTEM\CurrentControlSet\Services\hidusb\Parameters" /v "EnablePowerManagement" /t REG_DWORD /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "EnablePME" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "AutoDisablingGigabit" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "EnableGreenEthernet" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "EnableSavePowerNow" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "EnablePowerManagement" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "PowerDownPll" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "PowerSavingMode" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "ReduceSpeedOnPowerDown" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "S5NicKeepOverrideMacAddrV2" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "EnableConnectedPowerGating" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "GigaLite" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "ULPMode" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "WakeOnDisconnect" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "*WakeOnMagicPacket" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "*WakeOnPattern" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "WakeOnLink" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "WolShutdownLinkSpeed" /t REG_SZ /d "2" /f >nul 2>&1 
Reg.exe add "%%n" /v "LsoV1IPv4" /t REG_SZ /d "%_R_NIC%" /f >nul 2>&1 
Reg.exe add "%%n" /v "LsoV2IPv4" /t REG_SZ /d "%_R_NIC%" /f >nul 2>&1 
Reg.exe add "%%n" /v "LsoV2IPv6" /t REG_SZ /d "%_R_NIC%" /f >nul 2>&1 
Reg.exe add "%%n" /v "RxAbsIntDelay" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "TxIntDelay" /t REG_SZ /d "0" /f >nul 2>&1 
Reg.exe add "%%n" /v "TxAbsIntDelay" /t REG_SZ /d "0" /f >nul 2>&1 

REM === SERVICIOS DE RED ===
sc config "Wcmsvc" start=disabled >nul
sc config "NcaSvc" start=demand >nul
sc config "NetSetupSvc" start=demand >nul
sc config "iphlpsvc" start=disabled >nul
sc config "BthAvctpSvc" start=disabled >nul
sc config "BthHFSrv" start=disabled >nul
sc config "BTAGService" start=manual >nul
sc config "bthserv" start=manual >nul
sc config "Netlogon" start=disabled >nul
sc config "Netman" start=disabled >nul
sc config "WwanSvc" start=disabled >nul
sc config "wcncsvc" start=disabled >nul
sc config "Dhcp" start=auto >nul
sc config "Dnscache" start=auto >nul
sc config "NlaSvc" start=auto >nul
sc config "WlanSvc" start=auto >nul
sc config "netprofm" start=demand >nul
sc config "BluetoothUserService" start=demand >nul
net stop BthAvctpSvc >nul 2>&1 
sc config "Dnscache" start= demand >nul 2>&1 
sc start "Dnscache" >nul 2>&1 
for /f "tokens=3" %%a in ('sc queryex "Dnscache" ^| findstr "PID"') do (set pid=%%a) 
sc start Dnscache >nul 2>&1 
sc config Dnscache start=auto >nul 2>&1 
sc config Netlogon start=disabled >nul 2>&1 
sc config iphlpsvc start=disabled >nul 2>&1 
sc config wcncsvc start=disabled >nul 2>&1 
sc config bthserv start=disabled >nul 2>&1 
sc config BthAvctpSvc start=disabled >nul 2>&1 
sc config iphlpsvc start= disabled >nul 2>&1 
sc config BthAvctpSvc start= disabled >nul 2>&1 
sc config Wcmsvc start= disabled >nul 2>&1 
sc config BTAGService start= disabled >nul 2>&1 
sc config bthserv start= disabled >nul 2>&1 
sc config "Wcmsvc" start=disabled >nul 2>&1 
sc config "NcaSvc" start=demand >nul 2>&1 
sc config "NetSetupSvc" start=demand >nul 2>&1 
sc config "BthAvctpSvc" start= demand >nul 2>&1 
sc config "NcaSvc" start= demand >nul 2>&1 
sc config "Netlogon" start= demand >nul 2>&1 
sc config "Netman" start= demand >nul 2>&1 
sc config "NetSetupSvc" start= demand >nul 2>&1 
sc config "NlaSvc" start= demand >nul 2>&1 
sc config "Wcmsvc" start= demand >nul 2>&1 
sc config "wcncsvc" start= demand >nul 2>&1 
sc config "WlanSvc" start= demand >nul 2>&1 
sc config "WwanSvc" start= demand >nul 2>&1 
sc stop iphlpsvc >nul 2>&1 
sc stop wcncsvc >nul 2>&1 
sc config wwansvc start=disabled >nul 2>&1 
sc stop wwansvc >nul 2>&1 
sc config Dhcp start=auto >nul 2>&1 
sc config NlaSvc start=auto >nul 2>&1 
sc config WlanSvc start=auto >nul 2>&1 
sc config netprofm start=demand >nul 2>&1 
sc config bthserv start=demand >nul 2>&1 
sc config BTAGService start=demand >nul 2>&1 
sc config BluetoothUserService start=demand >nul 2>&1 
sc config Wcmsvc start=disabled >nul 2>&1 
sc config BthHFSrv start=disabled >nul 2>&1 
sc config BTAGService start=disabled >nul 2>&1 
sc config NcaSvc start=disabled >nul 2>&1 
sc config Netman start=disabled >nul 2>&1 
sc config NetSetupSvc start=disabled >nul 2>&1 
sc config "NcdAutoSetup" start=disabled >nul
sc config "NcdAutoSetup" start=disabled >nul 2>&1 
sc config NcdAutoSetup start=disabled >nul 2>&1 
sc config "NcdAutoSetup" start=demand >nul 2>&1 
sc config "NcdAutoSetup" start= demand >nul 2>&1 
sc stop NcdAutoSetup >nul 2>&1 

REM === SEGURIDAD DE RED ===
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Server' /v 'Enabled' /t 'REG_DWORD' /d '0' /f"
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server' /v 'Enabled' /t 'REG_DWORD' /d '0' /f"
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server' /v 'Enabled' /t 'REG_DWORD' /d '0' /f"
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server' /v 'Enabled' /t 'REG_DWORD' /d '0' /f"
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server' /v 'Enabled' /t 'REG_DWORD' /d '1' /f"
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Server' /v 'Enabled' /t 'REG_DWORD' /d '1' /f"
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Server' /v 'Enabled' /t 'REG_DWORD' /d '0' /f" >nul 2>&1 
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server' /v 'Enabled' /t 'REG_DWORD' /d '0' /f" >nul 2>&1 
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server' /v 'Enabled' /t 'REG_DWORD' /d '0' /f" >nul 2>&1 
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server' /v 'Enabled' /t 'REG_DWORD' /d '0' /f" >nul 2>&1 
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3\Server' /v 'Enabled' /t 'REG_DWORD' /d '1' /f" >nul 2>&1 
PowerShell -ExecutionPolicy Unrestricted -Command "reg add 'HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server' /v 'Enabled' /t 'REG_DWORD' /d '1' /f" >nul 2>&1 
Reg.exe add "HKLM\Software\Microsoft\PolicyManager\default\WiFi\AllowAutoConnectToWiFiSenseHotspots" /v "value" /t REG_DWORD /d "0" /f >nul 2>&1 
reg add "HKLM\Software\Microsoft\PolicyManager\default\WiFi\AllowAutoConnectToWiFiSenseHotspots" /v "value" /t REG_DWORD /d "0" /f >nul 2>&1