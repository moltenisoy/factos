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


def apply_telemetry():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'sc config DiagTrack start=disabled',
        r'sc stop DiagTrack',
        r'sc config dmwappushservice start=disabled',
        r'sc stop dmwappushservice',
        r'sc config diagnosticshub.standardcollector.service start=disabled',
        r'sc stop diagnosticshub.standardcollector.service',
        r'sc config WerSvc start=disabled',
        r'sc stop WerSvc',
        r'sc config wercplsupport start=disabled',
        r'sc stop wercplsupport',
        r'sc config DPS start=disabled',
        r'sc stop DPS',
        r'sc config PcaSvc start=disabled',
        r'sc stop PcaSvc',
        r'sc config WdiServiceHost start=disabled',
        r'sc stop WdiServiceHost',
        r'sc config WdiSystemHost start=disabled',
        r'sc stop WdiSystemHost',
        r'sc config diagsvc start=disabled',
        r'sc stop diagsvc',
        r'sc config wlidsvc start=disabled',
        r'sc stop wlidsvc',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v DisableEnterpriseAuthProxy /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v LimitDiagnosticLogCollection /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v DisableOneSettingsDownloads /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v DoNotShowFeedbackNotifications /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection" /v MaxTelemetryAllowed /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection" /v MicrosoftEdgeDataOptIn /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\DataCollection" /v MaxTelemetryAllowed /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\DiagTrack" /v Start /t REG_DWORD /d 4 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\dmwappushservice" /v Start /t REG_DWORD /d 4 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\WerSvc" /v Start /t REG_DWORD /d 4 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\diagnosticshub.standardcollector.service" /v Start /t REG_DWORD /d 4 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack" /v ShowedToastAtLevel /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack" /v DiagTrackStatus /t REG_DWORD /d 2 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\AppCompat" /v DisableInventory /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\AppCompat" /v AITEnable /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\AppCompat" /v DisablePCA /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\AppCompat" /v DisableEngine /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\AppCompat" /v DisableUAR /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\HandwritingErrorReports" /v PreventHandwritingErrorReports /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting" /v Disabled /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting" /v DontSendAdditionalData /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting" /v LoggingDisabled /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting" /v Disabled /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting" /v DontSendAdditionalData /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting" /v LoggingDisabled /t REG_DWORD /d 1 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\Windows Error Reporting" /v Disabled /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\SQMClient\Windows" /v CEIPEnable /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\SQMClient\Windows" /v CEIPEnable /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Siuf\Rules" /v NumberOfSIUFInPeriod /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Siuf\Rules" /v PeriodInNanoSeconds /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\AppCompat" /v DisableWindowsTracing /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v EnableActivityFeed /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v PublishUserActivities /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v UploadUserActivities /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy" /v TailoredExperiencesWithDiagnosticDataEnabled /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Application-Experience/Program-Telemetry" /v Enabled /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\AdvertisingInfo" /v DisabledByGroupPolicy /t REG_DWORD /d 1 /f',
        r'reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo" /v Enabled /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\TabletPC" /v PreventHandwritingDataSharing /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\IMM" /v DisableImeSentinels /t REG_DWORD /d 1 /f',
        r'schtasks /Change /TN "Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Application Experience\ProgramDataUpdater" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Application Experience\AitAgent" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Application Experience\StartupAppTask" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Customer Experience Improvement Program\Consolidator" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Customer Experience Improvement Program\UsbCeip" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Autochk\Proxy" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Feedback\Siuf\DmClient" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Windows Error Reporting\QueueReporting" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Device Information\Device" /Disable',
        r'schtasks /Change /TN "Microsoft\Windows\Device Information\Device User" /Disable',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\TabletPC" /v PreventHandwritingErrorReports /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Messenger\Client" /v CEIP /t REG_DWORD /d 2 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowDesktopAnalyticsProcessing /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowCommercialDataPipeline /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowWUfBCloudProcessing /t REG_DWORD /d 0 /f',
    ]

    for cmd in commands:
        run(cmd)


if __name__ == "__main__":
    apply_telemetry()
