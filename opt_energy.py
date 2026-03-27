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


def apply_energy_performance():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c',
        r'powercfg /change standby-timeout-ac 0',
        r'powercfg /change standby-timeout-dc 0',
        r'powercfg /change monitor-timeout-ac 0',
        r'powercfg /change monitor-timeout-dc 0',
        r'powercfg /change disk-timeout-ac 0',
        r'powercfg /change disk-timeout-dc 0',
        r'powercfg /change hibernate-timeout-ac 0',
        r'powercfg /change hibernate-timeout-dc 0',
        r'powercfg /hibernate off',
        r'powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 100',
        r'powercfg /setdcvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 100',
        r'powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 bc5038f7-23e0-4960-96da-33abaf5935ec 100',
        r'powercfg /setdcvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 bc5038f7-23e0-4960-96da-33abaf5935ec 100',
        r'powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 be337238-0d82-4146-a960-4f3749d470c7 2',
        r'powercfg /setdcvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 54533251-82be-4824-96c1-47b60b740d00 be337238-0d82-4146-a960-4f3749d470c7 2',
        r'powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0',
        r'powercfg /setdcvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0',
        r'powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 0',
        r'powercfg /setdcvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 0',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v PowerThrottlingOff /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v HibernateEnabled /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v HiberbootEnabled /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\be337238-0d82-4146-a960-4f3749d470c7" /v ValueMax /t REG_DWORD /d 2 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\be337238-0d82-4146-a960-4f3749d470c7" /v ValueMin /t REG_DWORD /d 2 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\be337238-0d82-4146-a960-4f3749d470c7" /v ValueUnits /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\intelppm" /v Start /t REG_DWORD /d 4 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\amdppm" /v Start /t REG_DWORD /d 4 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\processor" /v Start /t REG_DWORD /d 4 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v HiberbootEnabled /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Power\PowerSettings\94ac6d29-73ce-41a6-809f-6363ba21b47e" /v ACSettingIndex /t REG_DWORD /d 0 /f',
        r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Power\PowerSettings\94ac6d29-73ce-41a6-809f-6363ba21b47e" /v DCSettingIndex /t REG_DWORD /d 0 /f',
    ]

    for cmd in commands:
        run(cmd)


def apply_energy_saving():
    if os.name != "nt":
        sys.exit(1)

    commands = [
        r'powercfg /setactive a1841308-3541-4fab-bc81-f71556f20b4a',
        r'powercfg /change standby-timeout-ac 15',
        r'powercfg /change standby-timeout-dc 5',
        r'powercfg /change monitor-timeout-ac 10',
        r'powercfg /change monitor-timeout-dc 3',
        r'powercfg /change disk-timeout-ac 20',
        r'powercfg /change disk-timeout-dc 10',
        r'powercfg /hibernate on',
        r'powercfg /setacvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 5',
        r'powercfg /setdcvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 5',
        r'powercfg /setacvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 54533251-82be-4824-96c1-47b60b740d00 bc5038f7-23e0-4960-96da-33abaf5935ec 100',
        r'powercfg /setdcvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 54533251-82be-4824-96c1-47b60b740d00 bc5038f7-23e0-4960-96da-33abaf5935ec 50',
        r'powercfg /setacvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 54533251-82be-4824-96c1-47b60b740d00 be337238-0d82-4146-a960-4f3749d470c7 0',
        r'powercfg /setdcvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 54533251-82be-4824-96c1-47b60b740d00 be337238-0d82-4146-a960-4f3749d470c7 0',
        r'powercfg /setacvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 2',
        r'powercfg /setdcvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 3',
        r'powercfg /setacvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 2',
        r'powercfg /setdcvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 3',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v HibernateEnabled /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v HiberbootEnabled /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\intelppm" /v Start /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\amdppm" /v Start /t REG_DWORD /d 1 /f',
        r'reg add "HKLM\SYSTEM\CurrentControlSet\Services\processor" /v Start /t REG_DWORD /d 1 /f',
    ]

    for cmd in commands:
        run(cmd)


def apply_energy(mode="performance"):
    if mode == "saving":
        apply_energy_saving()
    else:
        apply_energy_performance()


if __name__ == "__main__":
    apply_energy("performance")
