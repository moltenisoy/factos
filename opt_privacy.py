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


def apply_privacy():
    """Optimizaciones de privacidad: Desactivar telemetría, diagnósticos y seguimiento"""
    if os.name != "nt":
        sys.exit(1)

    # Disable DiagTrack service
    run("sc stop DiagTrack")
    run("sc config DiagTrack start= Disabled")
    run("sc config \"DiagTrack\" start=disabled")
    run("reg.exe add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\DiagTrack\" /V \"Start\" /t REG_DWORD /d \"4\" /f")
    run("net stop \"DiagTrack\"")
    run("net stop DiagTrack")
    run("sc stop \"DiagTrack\"")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\DiagTrack\" /v \"Start\" /t REG_DWORD /d \"4\" /f")
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Diagnostics\\DiagTrack\" /v \"DiagTrackStatus\" /t REG_DWORD /d \"2\" /f")
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Diagnostics\\DiagTrack\" /v \"ShowedToastAtLevel\" /t REG_DWORD /d \"1\" /f")
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Diagnostics\\DiagTrack\" /v \"UploadPermissionReceived\" /t REG_DWORD /d \"1\" /f")
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Diagnostics\\DiagTrack\" /v \"DiagTrackAuthorization\" /t REG_DWORD /d \"775\" /f")
    run("Reg.exe add \"HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Diagnostics\\DiagTrack\" /v \"ShowedToastAtLevel\" /t REG_DWORD /d \"1\" /f")
    run("reg.exe add \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Diagnostics\\DiagTrack\\EventTranscriptKey\" /V \"EnableEventTranscript\" /t REG_DWORD /d \"0\" /f")

    # Disable telemetry
    run("Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\" /v \"AllowTelemetry\" /t REG_DWORD /d \"0\" /f")
    run("Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\" /v \"AllowDeviceNameInTelemetry\" /t REG_DWORD /d \"0\" /f")
    run("Reg.exe add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection\" /v \"AllowTelemetry\" /t REG_DWORD /d \"0\" /f")
    run("Reg.exe add \"HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection\" /v \"AllowTelemetry\" /t REG_DWORD /d \"0\" /f")
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection\" /v \"AllowDeviceNameInTelemetry\" /t REG_DWORD /d \"0\" /f")
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection\" /v \"MaxTelemetryAllowed\" /t REG_DWORD /d \"1\" /f")
    run("REG ADD \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\" /v \"AllowTelemetry\" /t REG_DWORD /d 0 /f")

    # Disable advertising ID
    run("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo\" /v \"Enabled\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AdvertisingInfo\" /v \"DisabledByGroupPolicy\" /t REG_DWORD /d 1 /f")

    # Disable cloud content
    run("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" /v \"SilentInstalledAppsEnabled\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" /v \"SubscribedContent-338393Enabled\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" /v \"SubscribedContent-353694Enabled\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" /v \"SubscribedContent-353696Enabled\" /t REG_DWORD /d 0 /f")

    # Disable location tracking
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location\" /v \"Value\" /t REG_SZ /d \"Deny\" /f")
    run(
        "reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Sensor\\Overrides\\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}\" /v \"SensorPermissionState\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\lfsvc\\Service\\Configuration\" /v \"Status\" /t REG_DWORD /d 0 /f")

    # Disable feedback
    run("reg add \"HKCU\\Software\\Microsoft\\Siuf\\Rules\" /v \"NumberOfSIUFInPeriod\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\" /v \"DoNotShowFeedbackNotifications\" /t REG_DWORD /d 1 /f")

    # Disable camera and microphone access
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\webcam\" /v \"Value\" /t REG_SZ /d \"Deny\" /f")
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\microphone\" /v \"Value\" /t REG_SZ /d \"Deny\" /f")

    # Disable activity history
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System\" /v \"EnableActivityFeed\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System\" /v \"PublishUserActivities\" /t REG_DWORD /d 0 /f")
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System\" /v \"UploadUserActivities\" /t REG_DWORD /d 0 /f")

    # Disable Windows Error Reporting
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\Windows Error Reporting\" /v \"Disabled\" /t REG_DWORD /d 1 /f")
    run("reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\Windows Error Reporting\" /v \"DontSendAdditionalData\" /t REG_DWORD /d 1 /f")

    # Disable Customer Experience Improvement Program
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator\" /disable")
    run("schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip\" /disable")

    # Disable Windows tips
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CloudContent\" /v \"DisableSoftLanding\" /t REG_DWORD /d 1 /f")
    run("reg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CloudContent\" /v \"DisableWindowsConsumerFeatures\" /t REG_DWORD /d 1 /f")
