import subprocess
from django.conf import settings
from django.http import HttpResponse

def websim(request):
  data = subprocess.run(
    ["python", "websim.py", settings.BASE_DIR / "bioinses/media"],
    capture_output=True, text=True
  ).stdout
  return HttpResponse(data, content_type="application/json")
