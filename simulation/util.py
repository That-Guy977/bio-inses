from __future__ import annotations
import math, random
from pygame.math import Vector2, clamp

name = "BIO-INSES"

size = Vector2(500, 500)

tlimit = 1000

out_dir = "simulation"

class Point(Vector2):
  def truncate(self):
    self.x = float(int(self.x))
    self.y = float(int(self.y))
    return self

  def clamp(self):
    self.x = clamp(self.x, 0, size.x)
    self.y = clamp(self.y, 0, size.y)
    return self

  def direction(self, pos) -> float:
    return math.degrees(math.atan2(pos.y - self.y, pos.x - self.x))

  def __str__(self):
    return f"({self.x:3.0f}, {self.y:3.0f})"

  @classmethod
  def polar(cls, r: float, phi: float):
    v = cls()
    v.from_polar((r, phi))
    return v

  @classmethod
  def random(cls):
    return cls([random.randint(0, dim) for dim in size])

def deviate(m: int, s: int):
  return m + random.randint(-s, s)
