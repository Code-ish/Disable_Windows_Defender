import os
import winreg

# Function to remove Windows Defender from the system
def remove_windows_defender():
    try:
        # Set the registry key for Windows Defender
        key_path = r"Software\Policies\Microsoft\Windows Defender"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)

        # Set the values to disable Windows Defender
        winreg.SetValueEx(key, "DisableAntiSpyware", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "DisableAntiVirus", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "DisableRealtimeMonitoring", 0, winreg.REG_DWORD, 1)

        # Close the registry key
        winreg.CloseKey(key)

        # Remove Windows Defender from the system
        os.system("wscui.cpl /DisableAntiSpyware")
        os.system("wscui.cpl /DisableAntiVirus")
        os.system("wscui.cpl /DisableRealtimeMonitoring")

        print("Windows Defender has been removed from the system.")

    except Exception as e:
        print(f"An error occurred while removing Windows Defender: {e}")

# Call the function to remove Windows Defender
remove_windows_defender()