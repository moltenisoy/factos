import subprocess
import os
import sys
from backup_mgr_comprehensive import create_comprehensive_backup, restore_from_comprehensive_backup


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


def apply_graphics():
    """Optimizaciones de gráficos: GPU, drivers, y rendimiento visual"""
    if os.name != "nt":
        sys.exit(1)

    # Extract all commands to pass to backup system
    commands_to_apply = [
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"GCOOPTION_DisableGPIOPowerSaveMode\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""reg add \\\"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"EnableAeroPeek\\\" /t REG_DWORD /d 0 /f 2""",
        r"""reg add \\\"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"Animations\\\" /t REG_DWORD /d 0 /f 2""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PowerThrottling\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableUlps\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableULPS\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"AnimationAttributionEnabled\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"AnimationAttributionHashingEnabled\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKLM\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"DisallowAnimations\\\" /t REG_DWORD /d 1 /f""",
        r"""reg add \\\"HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\Dwm\\\" /v \\\"AnimationAttributionEnabled\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\Dwm\\\" /v \\\"AnimationAttributionHashingEnabled\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\stornvme\\\\Parameters\\\\Device\\\" /v \\\"LowLatencyMode\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKCU\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\VisualEffects\\\\DWMAeroPeekEnabled\\\" /v \\\"DefaultApplied\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKCU\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\VisualEffects\\\\DWMEnabled\\\" /v \\\"DefaultApplied\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKCU\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\VisualEffects\\\\DWMSaveThumbnailEnabled\\\" /v \\\"DefaultApplied\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_GPUPowerDownEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RMGpuId\\\" /t REG_DWORD /d \\\"256\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"GPUPreemptionLevel\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableMidGfxPreemptionVGPU\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableMidBufferPreemptionForHighTdrTimeout\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"Composition\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\Dwm\\\" /v \\\"OneCoreNoComposition\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""reg add \\\"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"Composition\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\Dwm\\\" /v \\\"OneCoreNoComposition\\\" /t REG_DWORD /d 1 /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_GPUPowerDownEnabled\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKCU\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"UseDpiScaling\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"EnableAeroPeek\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg.exe add \\\"HKEY_CURRENT_USER\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /V \\\"EnableAeroPeek\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg.exe add \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\DWM\\\" /V \\\"DWMWA_TRANSITIONS_FORCEDISABLED\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""reg.exe add \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\DWM\\\" /V \\\"DisallowAnimations\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"DWMWA_TRANSITIONS_FORCEDISABLED\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"DisallowAnimations\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableVceSwClockGating\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableUvdClockGating\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableVCEPowerGating\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableUVDPowerGatingDynamic\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisablePowerGating\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableSAMUPowerGating\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableFBCForFullScreenApp\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableFBCSupport\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableEarlySamuInit\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableDrmdmaPowerGating\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_SclkDeepSleepDisable\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_ActivityTarget\\\" /t REG_DWORD /d \\\"30\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_ODNFeatureEnable\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableUlps\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_AllGraphicLevel_DownHyst\\\" /t REG_DWORD /d \\\"20\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_AllGraphicLevel_UpHyst\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"KMD_FRTEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableDMACopy\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableBlockWrite\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"KMD_MaxUVDSessions\\\" /t REG_DWORD /d \\\"32\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DalAllowDirectMemoryAccessTrig\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DalAllowDPrefSwitchingForGLSync\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"WmAgpMaxIdleClk\\\" /t REG_DWORD /d \\\"32\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_MCLKStutterModeThreshold\\\" /t REG_DWORD /d \\\"4096\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"StutterMode\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"TVEnableOverscan\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\Dwm\\\" /v \\\"OverlayTestMode\\\" /t REG_DWORD /d \\\"5\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"MLF\\\" /t REG_BINARY /d \\\"3000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"EQAA\\\" /t REG_BINARY /d \\\"3000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"PowerState\\\" /t REG_BINARY /d \\\"3000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"AreaAniso_DEF\\\" /t REG_SZ /d \\\"8\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"SurfaceFormatReplacements_DEF\\\" /t REG_SZ /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"Main3D_DEF\\\" /t REG_SZ /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"AnisoType_DEF\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"AnisoDegree_DEF\\\" /t REG_SZ /d \\\"4\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"ForceTripleBuffering\\\" /t REG_BINARY /d \\\"3000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"ForceTripleBuffering_DEF\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TextureOpt_DEF\\\" /t REG_SZ /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TextureLod_DEF\\\" /t REG_SZ /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TruformMode_DEF\\\" /t REG_SZ /d \\\"2\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"LodAdj\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"ForceZBufferDepth_DEF\\\" /t REG_SZ /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"Tessellation_OPTION_DEF\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"NoOSPowerOptions\\\" /t REG_SZ /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"ForceZBufferDepth\\\" /t REG_BINARY /d \\\"3100\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"Tessellation_DEF\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"Main3D\\\" /t REG_BINARY /d \\\"3100\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"AnisoType\\\" /t REG_BINARY /d \\\"32000000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"AnisotropyOptimise\\\" /t REG_BINARY /d \\\"3100\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TrilinearOptimise\\\" /t REG_BINARY /d \\\"3100\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"AnisoDegree\\\" /t REG_BINARY /d \\\"3400\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TextureLod\\\" /t REG_BINARY /d \\\"31000000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TextureOpt\\\" /t REG_BINARY /d \\\"31000000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TruformMode_NA\\\" /t REG_BINARY /d \\\"3200\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"Tessellation_OPTION\\\" /t REG_BINARY /d \\\"3200\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"Tessellation\\\" /t REG_BINARY /d \\\"3100\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"Main3D_SET\\\" /t REG_BINARY /d \\\"302031203220332034203500\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"ForceZBufferDepth_SET\\\" /t REG_BINARY /d \\\"3020313620323400\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"FlipQueueSize\\\" /t REG_SZ /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"SurfaceFormatReplacements\\\" /t REG_BINARY /d \\\"3000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TFQ\\\" /t REG_BINARY /d \\\"3200\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TFQ_DEF\\\" /t REG_SZ /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"ZFormats_NA\\\" /t REG_BINARY /d \\\"3100\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"AntiStuttering\\\" /t REG_BINARY /d \\\"3000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"TurboSync\\\" /t REG_BINARY /d \\\"3000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"HighQualityAF\\\" /t REG_BINARY /d \\\"3300\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"ShaderCache\\\" /t REG_BINARY /d \\\"3200\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\ControlSet001\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableUlps\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DesktopStereoShortcuts\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"FeatureControl\\\" /t REG_DWORD /d \\\"4\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"NVDeviceSupportKFilter\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RmCacheLoc\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RmDisableInst2Sys\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RmFbsrPagedDMA\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RmProfilingAdminOnly\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"TCCSupported\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"TrackResetEngine\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"UseBestResolution\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"ValidateBlitSubRects\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Power\\\" /v \\\"LowLatencyScalingPercentage\\\" /t REG_DWORD /d \\\"100\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnablePreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"ComputePreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableAsyncMidBufferPreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableSCGMidBufferPreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PerfAnalyzeMidBufferPreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableMidGfxPreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableMidBufferPreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableCEPreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""reg add \\\"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"EnableAeroPeek\\\" /t REG_DWORD /d 0 /f""",
        r"""REG ADD \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Policies\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"DisallowAnimations\\\" /t REG_DWORD /d 1 /f""",
        r"""REG ADD \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\Dwm\\\" /v \\\"AnimationAttributionEnabled\\\" /t REG_DWORD /d 0 /f""",
        r"""REG ADD \\\"HKEY_LOCAL_MACHINE\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\Dwm\\\" /v \\\"AnimationAttributionHashingEnabled\\\" /t REG_DWORD /d 0 /f""",
        r"""REG ADD \\\"HKEY_CURRENT_USER\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"AnimationAttributionEnabled\\\" /t REG_DWORD /d 0 /f""",
        r"""REG ADD \\\"HKEY_CURRENT_USER\\\\Software\\\\Microsoft\\\\Windows\\\\DWM\\\" /v \\\"AnimationAttributionHashingEnabled\\\" /t REG_DWORD /d 0 /f""",
        r"""reg add \\\"HKEY_LOCAL_MACHINE\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnableUlps\\\" /t REG_DWORD /d 0 /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PreferSystemMemoryContiguous\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\System\\\\ControlSet001\\\\Control\\\\Class\\\\%%m\\\" /v \\\"RMHdcpKeyglobZero\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"D3PCLatency\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"F1TransitionLatency\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"LOWLATENCY\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"Node3DLowLatency\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PciLatencyTimerControl\\\" /t REG_DWORD /d \\\"20\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RMDeepL1EntryLatencyUsec\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RmGspcMaxFtuS\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RmGspcMinFtuS\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RmGspcPerioduS\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RMLpwrEiIdleThresholdUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RMLpwrGrIdleThresholdUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RMLpwrGrRgIdleThresholdUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"RMLpwrMsIdleThresholdUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"VRDirectFlipDPCDelayUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"VRDirectFlipTimingMarginUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"VRDirectJITFlipMsHybridFlipDelayUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"vrrCursorMarginUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"vrrDeflickerMarginUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"vrrDeflickerMaxUs\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\\\\\DAL2_DATA__2_0\\\\DisplayPath_4\\\\EDID_D109_78E9\\\\Option\\\" /v \\\"ProtectionControl\\\" /t REG_BINARY /d \\\"0100000001000000\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"3D_Refresh_Rate_Override_DEF\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"AllowSnapshot\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"AAF_NA\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"ASTT_NA\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"AllowSubscription\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"AreaAniso_NA\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"AllowRSOverlay\\\" /t REG_SZ /d \\\"false\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"Adaptive De-interlacing\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"AllowSkins\\\" /t REG_SZ /d \\\"false\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"AutoColorDepthReduction_NA\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableUVDPowerGatingDynamic\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"DisableVCEPowerGating\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnablingVceSwClockGating\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnablingUvdClockGating\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnablingAspmL0s\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnablingAspmL1\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnablingUlps\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"EnablingUlps_NA\\\" /t REG_SZ /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"KMD_DeLagEnabled\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"KMD_EnableComputePreemption\\\" /t REG_DWORD /d \\\"0\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\\UMD\\\" /v \\\"FlipQueueSize\\\" /t REG_BINARY /d \\\"3100\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\amdlog\\\" /v \\\"Start\\\" /t REG_DWORD /d \\\"4\\\" /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_ThermalAutoThrottlingEnable\\\" /t REG_DWORD /d \\\"1\\\" /f""",
        r"""reg add \\\"HKEY_LOCAL_MACHINE\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PowerThrottling\\\" /t REG_DWORD /d 0 /f""",
        r"""Reg.exe add \\\"HKLM\\\\SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\\0000\\\" /v \\\"PP_ThermalAutoThrottlingEnabled\\\" /t REG_DWORD /d \\\"0\\\" /f""",
    ]
    
    # Create comprehensive backup BEFORE applying optimizations
    print(f"Creating comprehensive backup for graphics...")
    backup_info = create_comprehensive_backup("graphics", commands_to_apply)
    print(f"Backup created: {{backup_info['backed_up_items']}} items backed up")
    print(f"Backup directory: {{backup_info['backup_directory']}}")
    
    # Now apply all optimizations
    print(f"Applying graphics optimizations...")
    for cmd in commands_to_apply:
        run(cmd)
    
    print(f"{category_name.title()} optimizations completed!")
    return backup_info


def get_backup_data():
    return {{'backup_created': True}}


def restore_from_backup_data(backup_dir):
    if not backup_dir:
        return False
    return restore_from_comprehensive_backup(backup_dir)
