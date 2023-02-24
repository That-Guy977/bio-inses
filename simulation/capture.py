import os, subprocess
from Quartz import \
  CGWindowListCopyWindowInfo as COPY_WINDOW_INFO, \
  kCGWindowListOptionAll as OPTION_ALL, \
  kCGNullWindowID as NULL_WINDOW_ID, \
  kCGWindowNumber as WINDOW_NUMBER, \
  kCGWindowName as WINDOW_NAME, \
  kCGWindowOwnerName as WINDOW_OWNER_NAME
from .entity import Entity
from .util import name

MAX_ATTEMPTS = 5

window_id = None
out_dir = None

def save():
  if window_id is None:
    find_window()
  out_file = f"{out_dir}/{Entity.tick:04}.png"
  for _ in range(MAX_ATTEMPTS):
    res = subprocess.run(["screencapture", "-l", f"{window_id}", out_file], stderr=subprocess.DEVNULL)
    if res.returncode == 0:
      break
  else:
    subprocess.run(["cp", f"{out_dir}/{Entity.tick - 1:04}.png", out_file], stderr=subprocess.DEVNULL)

def find_window():
  windows = COPY_WINDOW_INFO(OPTION_ALL, NULL_WINDOW_ID)
  for window in windows:
    if WINDOW_NAME in window and window[WINDOW_NAME] == name \
      and WINDOW_OWNER_NAME in window and window[WINDOW_OWNER_NAME] == "Python":
        global window_id
        window_id = window[WINDOW_NUMBER]
        return
  raise LookupError("Window not found")

def set_outdir(outdir: str):
  global out_dir
  out_dir = f"{outdir}/{Entity.dt}"
  os.makedirs(out_dir, exist_ok=True)
