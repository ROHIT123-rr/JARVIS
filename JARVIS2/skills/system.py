import os
import subprocess
import webbrowser
from datetime import datetime
import ctypes
import time
from pathlib import Path
try:
    import pyautogui
except Exception:
    pyautogui = None


def shutdown_windows() -> None:
    os.system("shutdown /s /t 1")


def open_chrome() -> None:
    path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    if os.path.exists(path):
        subprocess.Popen([path])
    else:
        webbrowser.open("https://google.com")


def search_google(query: str) -> None:
    if not query:
        return
    webbrowser.open(f"https://www.google.com/search?q={query}")


def open_folder(folder_name: str) -> bool:
    if not folder_name:
        return False
    folder_path = os.path.join(os.path.expanduser("~"), folder_name)
    if os.path.exists(folder_path):
        os.startfile(folder_path)
        return True
    return False


def current_time() -> str:
    return datetime.now().strftime("%I:%M %p")


def restart_windows() -> None:
    os.system("shutdown /r /t 1")


def lock_windows() -> None:
    try:
        ctypes.windll.user32.LockWorkStation()
    except Exception:
        pass


def open_app_by_path(path: str) -> bool:
    if not path:
        return False
    expanded = os.path.expandvars(path)
    if os.path.exists(expanded):
        subprocess.Popen([expanded])
        return True
    return False


def screenshot_to_pictures() -> str:
    if not pyautogui:
        return "PyAutoGUI not available"
    pictures = Path(os.path.expanduser("~")) / "Pictures"
    pictures.mkdir(parents=True, exist_ok=True)
    file = pictures / f"screenshot_{int(time.time())}.png"
    img = pyautogui.screenshot()
    img.save(str(file))
    return str(file)

