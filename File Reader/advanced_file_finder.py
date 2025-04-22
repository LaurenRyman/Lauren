
# -----------------------------------------
# advanced_file_finder.py
# Author: Lauren Ryman
# Date: 03/22/25
# Description:
#   Elevates to admin/root if necessary, locates all fixed drives (Windows) or root (Unix),
#   then recursively searches for a given filename across the entire system.
# -----------------------------------------

import os
import sys
import ctypes
import string

def is_admin():
    """
    Returns True if the current process has administrative/root privileges.
    """
    try:
        if os.name == 'nt':
            # Windows: use Shell32.IsUserAnAdmin()
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
            # Unix: root has euid 0
            return os.geteuid() == 0
    except Exception:
        return False

def ensure_admin():
    """
    Relaunches the script with elevated privileges if not already running as admin/root.
    On Windows, this will pop the UAC prompt.
    On Unix, it will exit with a reminder.
    """
    if not is_admin():
        if os.name == 'nt':
            # Relaunch with "runas" verb to elevate
            params = " ".join([sys.executable] + sys.argv)
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            sys.exit(0)
        else:
            print("Error: This script must be run as root. Try again with sudo.")
            sys.exit(1)

def get_fixed_drives():
    """
    Returns a list of drive roots on Windows (only those present).
    On Unix, returns ['/'].
    """
    if os.name != 'nt':
        return [os.path.abspath(os.sep)]

    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for idx, letter in enumerate(string.ascii_uppercase):
        if bitmask & (1 << idx):
            drive = f"{letter}:\\"
            drives.append(drive)
    return drives

def find_file_everywhere(filename):
    """
    Elevates if needed, then searches every fixed drive (or / on Unix)
    for all occurrences of filename. Returns a list of full paths.
    """
    # Step 1: ensure we have permission to traverse system folders
    ensure_admin()

    matches = []
    for start in get_fixed_drives():
        for root, dirs, files in os.walk(start):
            if filename in files:
                matches.append(os.path.join(root, filename))
    return matches

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python advanced_file_finder.py <filename>")
        sys.exit(1)

    target = sys.argv[1]
    results = find_file_everywhere(target)

    if not results:
        print(f"No matches found for '{target}'.")
    else:
        print(f"Found {len(results)} file(s):")
        for path in results:
            print("  " + path)
