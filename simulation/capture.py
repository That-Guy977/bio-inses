from entity import Entity
from util import name
from Quartz import \
  CGWindowListCopyWindowInfo as COPY_WINDOW_INFO, \
  kCGWindowListOptionAll as OPTION_ALL, \
  kCGNullWindowID as NULL_WINDOW_ID, \
  kCGWindowNumber as WINDOW_NUMBER, \
  kCGWindowName as WINDOW_NAME, \
  kCGWindowOwnerName as WINDOW_OWNER_NAME
import subprocess

MAX_ATTEMPTS = 5

OUT_DIR = f"runs/{Entity.dt}"

window_id = None

def save() -> None:
  if window_id is None:
    find_window()
  outfile = f"{OUT_DIR}/{Entity.tick:04}.png"
  for _ in range(MAX_ATTEMPTS):
    res = subprocess.run(["screencapture", "-l", f"{window_id}", outfile], stderr=subprocess.DEVNULL)
    if res.returncode == 0:
      break
  else:
    subprocess.run(["cp", f"{OUT_DIR}/{Entity.tick - 1:04}.png", outfile], stderr=subprocess.DEVNULL)

def find_window() -> None:
  windows = COPY_WINDOW_INFO(OPTION_ALL, NULL_WINDOW_ID)
  for window in windows:
    if WINDOW_NAME in window and window[WINDOW_NAME] == name \
      and WINDOW_OWNER_NAME in window and window[WINDOW_OWNER_NAME] == "Python":
        global window_id
        window_id = window[WINDOW_NUMBER]
        return
  raise LookupError("Window not found")
