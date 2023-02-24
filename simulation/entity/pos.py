from entity.base import Entity
from entity.params import Params
from util import Point

class Position(Entity):
  params = Params(
    "POS",
    size = 0
  )

  def __init__(self, pos: Point):
    super().__init__(Position.params, pos, 0)

  def __str__(self):
    return f"{self.type}@{self.pos}"

  def __eq__(self, o):
    return isinstance(o, Entity) and self.pos == o.pos and self.type == o.type
