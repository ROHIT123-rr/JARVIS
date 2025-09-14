from typing import Callable, Optional, Tuple
import re
from skills import system as sys_skill


def parse_intent(command: str) -> Tuple[str, Optional[str]]:
    text = command.lower().strip()

    if any(k in text for k in ["exit", "quit", "stop", "bye", "goodbye"]):
        return ("exit", None)

    if "shutdown" in text or "shut down" in text:
        return ("shutdown", None)

    if "open chrome" in text:
        return ("open_chrome", None)

    m = re.search(r"(?:search for|google)\s+(.*)$", text)
    if m:
        return ("search_google", m.group(1).strip())

    m = re.search(r"open folder\s+(.*)$", text)
    if m:
        return ("open_folder", m.group(1).strip())

    if any(k in text for k in ["time", "current time", "what time"]):
        return ("time", None)

    if any(k in text for k in ["restart", "reboot"]):
        return ("restart", None)

    if any(k in text for k in ["lock pc", "lock computer", "lock screen"]):
        return ("lock", None)

    m = re.search(r"open app\s+(.*)$", text)
    if m:
        return ("open_app", m.group(1).strip())

    if any(k in text for k in ["screenshot", "take screenshot", "capture screen"]):
        return ("screenshot", None)

    return ("chat", command)


def dispatch(intent: str, arg: Optional[str]) -> Optional[str]:
    if intent == "exit":
        return "exit"
    if intent == "shutdown":
        sys_skill.shutdown_windows()
        return "Shutting down."
    if intent == "open_chrome":
        sys_skill.open_chrome()
        return "Opening Chrome."
    if intent == "search_google":
        sys_skill.search_google(arg or "")
        return f"Searching for {arg}."
    if intent == "open_folder":
        ok = sys_skill.open_folder(arg or "")
        return "Opening folder." if ok else "Folder not found."
    if intent == "time":
        return f"The time is {sys_skill.current_time()}"
    if intent == "restart":
        sys_skill.restart_windows()
        return "Restarting now."
    if intent == "lock":
        sys_skill.lock_windows()
        return "Locking the computer."
    if intent == "open_app":
        ok = sys_skill.open_app_by_path(arg or "")
        return "Opening application." if ok else "App path not found."
    if intent == "screenshot":
        path = sys_skill.screenshot_to_pictures()
        return f"Saved screenshot to {path}"
    return None


