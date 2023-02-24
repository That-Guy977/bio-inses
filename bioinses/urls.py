from django.urls import path, re_path
from django.shortcuts import render, redirect

urlpatterns = [
  path("", lambda req: render(req, "index.html"), name="home"),
  path("simulation/", lambda req: render(req, "simulation.html"), name="simulation"),
  path("detect/", lambda req: render(req, "detect.html"), name="detect"),
  path("favicon.ico", lambda req: redirect("/static/logo.png")),
  re_path(r"^.*$", lambda req: redirect("/"))
]
