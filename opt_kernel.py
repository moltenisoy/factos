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


def apply_kernel():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'bcdedit /set useplatformclock false',
        r'bcdedit /set useplatformtick yes',
        r'bcdedit /set disabledynamictick yes',
        r'bcdedit /set tscsyncpolicy enhanced',
        r'bcdedit /set hypervisorlaunchtype off',
        r'bcdedit /set nx OptIn',
        r'bcdedit /set pae Default',
        r'bcdedit /set linearaddress57 OptOut',
        r'bcdedit /set increaseuserva 3072',
        r'bcdedit /set isolatedcontext No',
        r'bcdedit /set allowedinmemorysettings 0x0',
        r'bcdedit /set vm No',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v DpcWatchdogPeriod /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v DpcTimeout /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v MinimumStackCommitInBytes /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v GlobalTimerResolutionRequests /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v DistributeTimers /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v DisableExceptionChainValidation /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v KernelSEHOPEnabled /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v MitigationOptions /t REG_QWORD /d 0x222222222222 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v MitigationAuditOptions /t REG_QWORD /d 0x0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SubSystems" /v Optional /t REG_MULTI_SZ /d "" /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d 26 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v IRQ8Priority /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v IRQ16Priority /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v IRQ24Priority /t REG_DWORD /d 1 /f',
        r'fsutil behavior set disable8dot3 1',
        r'fsutil behavior set disablelastaccess 1',
        r'fsutil behavior set mftzone 2',
        r'fsutil behavior set memoryusage 2',
        r'fsutil behavior set encryptpagingfile 0',
        r'fsutil behavior set quotanotify 100',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v NtfsDisable8dot3NameCreation /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v NtfsDisableLastAccessUpdate /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v NtfsMftZoneReservation /t REG_DWORD /d 2 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v ContigFileAllocSize /t REG_DWORD /d 64 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v AllocateDeletedFilesImmediately /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v ReservePoolNonPaged /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\NTFS\Parameters" /v NtfsDisable8dot3NameCreation /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\NTFS\Parameters" /v NtfsDisableLastAccessUpdate /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\NTFS\Parameters" /v NtfsMftZoneReservation /t REG_DWORD /d 2 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\NTFS\Parameters" /v Lookaside /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\NTFS\Parameters" /v CcDisableReadAheadOnSmallFiles /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v RunAsPPL /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v DisableRestrictedAdmin /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v NoLMHash /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v LimitBlankPasswordUse /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v crashonauditfail /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v EnableDynamicBacklog /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v MinimumDynamicBacklog /t REG_DWORD /d 128 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v MaximumDynamicBacklog /t REG_DWORD /d 2048 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v DynamicBacklogGrowthDelta /t REG_DWORD /d 128 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v DisablePagingExecutive /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f',
        r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v LazyModeTimeout /t REG_DWORD /d 100000 /f',

    ]

    for cmd in commands:
        run(cmd)


if __name__ == "__main__":
    apply_kernel()
