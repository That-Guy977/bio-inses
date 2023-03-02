import json
from subprocess import Popen, PIPE
from django.conf import settings
from django.http import JsonResponse, HttpResponseNotFound

runs: dict[str, Popen] = {}

def websim(request):
  proc = Popen(
    ["python", "-u", "websim.py", settings.BASE_DIR / "bioinses/media"],
    stdout=PIPE, text=True, bufsize=1
  )
  data = json.loads(proc.stdout.readline())
  run = data["dt"]
  runs[run] = proc
  return JsonResponse(data)

def simtick(request, run: str):
  print(request, run)
  if run in runs:
    data = json.loads(runs[run].stdout.readline())
    if data["done"]:
      del runs[run]
    return JsonResponse(data)
  else:
    return HttpResponseNotFound()
