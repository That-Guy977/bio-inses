from __future__ import annotations
from pygame.sprite import Group
from .base import Entity
from .insect import Insect
from .params import Params
from ..util import Point, size

class Trap(Entity):
  params = Params(
    "TRAP",
    size = 10,
    release = 200
  )

  traps: Group[Trap] = Group()

  def __init__(self, pos: Point):
    super().__init__(pos, 0x00FFFF)
    self.held = []
    none: Group[Entity] = None
    self.entities = none

  def update(self):
    for insc in self.entities:
      if isinstance(insc, Insect) and self.touch(insc):
        self.capture(insc)
    if Entity.tick and Entity.tick % self.params.release == 0:
      for insc in self.held:
        self.release(insc)
      self.held.clear()

  def capture(self, insc: Insect):
    self.held.append(insc)
    insc.remove()
    Entity.log(self, "trap", insc)

  def release(self, insc: Insect):
    insc.pos = Point.random()
    insc.mark()
    self.entities.add(insc)
    Entity.log(self, "rls", insc)

  def empty(self):
    return len(self) == 0

  def __len__(self):
    return len(self.held)

  def __bool__(self):
    return not self.empty()

  @classmethod
  def generate(cls):
    cls.traps.add(
      cls(Point(
        a * size.x // 4 - cls.params.size // 2,
        b * size.y // 4 - cls.params.size // 2
      ))
      for a in (1, 3)
      for b in (1, 3)
    )
    return cls.traps

  @classmethod
  def bind(cls, entities: Group[Entity]):
    for trap in cls.traps:
      trap.entities = entities
