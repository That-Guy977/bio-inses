from django.urls import path, re_path
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from .websim import websim

urlpatterns = [
  path("",            lambda request: render(request, "index.html"),      name="home"),
  path("simulation/", lambda request: render(request, "simulation.html"), name="simulation"),
  path("detect/",     lambda request: render(request, "detect.html"),     name="detect"),
  path("websim/",                     websim,                             name="websim"),
  *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
  path("favicon.ico", lambda request: redirect("/static/logo.png")),
  re_path(r"^.*$",    lambda request: redirect("/"))
]
