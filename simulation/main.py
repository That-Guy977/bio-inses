import random
import pygame
from pygame import display, Surface
from pygame.sprite import Group
from pygame.time import wait
from .entity import *
from .util import name, size, tlimit, out_dir
from .capture import save, set_outdir
from .weather import geocode
from typing import Sequence

__all__ = ["main", "init", "tick", "check_end", "dead"]

def main(seed: int = None):

  screen, entities, _ = init(seed)
  while True:
    tick(screen, entities)
    save()
    print(f"{Entity.tick:4} ; Pests: {Insect.counts['PEST']:3} ; Preds: {Insect.counts['PRED']:3} ; Trapped: {sum(map(len, Trap.traps)):3}", end="\r")
    check_end()
    wait(1)

def init(seed: int = None, outdir = out_dir):
  pygame.init()
  screen = display.set_mode(size)
  display.set_caption(name)
  if seed is None: seed = random.getrandbits(32)
  random.seed(seed)
  Entity.reset(f"{outdir}/logs")
  set_outdir(f"{outdir}/runs")
  # geocode("chiangmai,th")
  entities = Group(
    # Trap.generate(),
    Pest.generate(),
    Pred.generate(),
  )
  Trap.bind(entities)
  return screen, entities, seed

def tick(screen: Surface, entities: Group, cb = lambda: print()):
  Entity.next_tick()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      Entity.log("MAIN", "quit")
      pygame.quit()
      cb()
      exit()
  entities.clear(screen, lambda surf, rect: surf.fill(0, rect))
  entities.update()
  entities.draw(screen)
  display.update()

def check_end(tlim = tlimit):
  if Entity.tick >= tlim:
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    Entity.log("MAIN", "time")
    Entity.log("MAIN", "gsz", Insect.counts["PEST"], Insect.counts["PRED"])
  elif dead():
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    Entity.log("MAIN", "end")

def dead() -> bool:
  return not Insect.counts["PEST"] and not Insect.counts["PRED"] \
    and all(trap.empty() for trap in Trap.traps)
