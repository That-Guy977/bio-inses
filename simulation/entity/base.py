from __future__ import annotations
import os
from datetime import datetime
from pygame import Surface, Rect
from pygame.sprite import Sprite
from ..util import Point, size

class Entity(Sprite):
  def __init__(self, pos: Point, color: int):
    super().__init__()
    self.id = Entity.count
    self.params = self.__class__.params
    self.type = self.params.type
    self.size = self.params.size
    self.pos = pos
    self.image = Surface((self.size, self.size))
    self.image.fill(color)
    self.rect = Rect(self.pos.truncate(), (self.size, self.size))
    Entity.entities[self.id] = self
    Entity.count += 1

  def update(self) -> None:
    self.rect.update(self.pos.truncate().clamp(), self.rect.size)
    self.rect.clamp_ip((0, 0), size)

  def color(self, color: int) -> None:
    self.image.fill(color)

  def touch(self, target: Entity) -> bool:
    return self.center().distance_to(target.center()) <= self.params.size / 2 + target.params.size / 2

  def center(self) -> Point:
    return self.pos + Point(self.size) / 2

  def __str__(self):
    return f"{self.type}@{self.id:08x}"

  @classmethod
  def log(cls, ctx: Entity, act: str, *args) -> None:
    print(f"{cls.tick:4}:" if cls.ln else " " * 5, ctx, act.rjust(4), *args, file=cls.file)
    cls.ln = False

  @classmethod
  def next_tick(cls) -> None:
    cls.tick += 1
    cls.ln = True

  @classmethod
  def reset(cls, outdir: str) -> None:
    cls.tick = -1
    cls.count = 0
    cls.entities: dict[int, Entity] = {}
    os.makedirs(f"{outdir}", exist_ok=True)
    cls.dt = f"{datetime.now():%Y%m%d-%H%M%S}"
    cls.file = open(f"{outdir}/{cls.dt}.bioinses", "w", 1)
    cls.ln = True
