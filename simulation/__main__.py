import pygame
from pygame import display, Surface
from pygame.sprite import Group
from pygame.time import wait
from entity import *
from util import name, size, tlimit
from capture import save
from weather import geocode
from typing import Sequence
import os, random

def main(seed: int = None):
  os.makedirs("simulation/logs", exist_ok=True)
  os.makedirs(f"simulation/runs/{Entity.dt}", exist_ok=True)
  screen, (entities, pests, preds, traps) = init(seed)
  while True:
    tick(screen, entities)
    save()
    print(f"{Entity.tick:4} ; Pests: {len(pests):3} ; Preds: {len(preds):3} ; Trapped: {sum(map(len, Trap.traps)):3}", end="\r")
    check_end(pests, preds, traps)
    wait(1)

def init(seed: int):
  pygame.init()
  screen = display.set_mode(size)
  display.set_caption(name)
  random.seed(seed)
  # geocode("chiangmai,th")
  entities: Group = Group()
  traps = None
  entities.add(
    # traps := Trap.generate(),
    pests := Pest.generate(),
    preds := Pred.generate(),
  )
  Trap.bind(pests, preds, entities)
  return screen, (entities, pests, preds, traps)

def tick(screen: Surface, entities: Group):
  Entity.next_tick()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      Entity.log("MAIN", "quit")
      print()
      pygame.quit()
      exit()
  entities.clear(screen, lambda surf, rect: surf.fill(0, rect))
  entities.update()
  entities.draw(screen)
  display.update()

def check_end(pests: Sequence[Pest], preds: Sequence[Pred], traps: Sequence[Trap]):
  if Entity.tick >= tlimit:
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    Entity.log("MAIN", "time")
    Entity.log("MAIN", "gsz", len(pests), len(preds))
  elif dead(pests, preds, traps):
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    Entity.log("MAIN", "end")

def dead(pests: Sequence[Pest], preds: Sequence[Pred], traps: Sequence[Trap]) -> bool:
  return not pests and not preds \
    and (not traps or all(trap.empty() for trap in traps))

if __name__ == "__main__":
  main(127)
