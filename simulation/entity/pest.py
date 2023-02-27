from .base import Entity
from .insect import Insect
from .params import Params
from ..util import Point

class Pest(Insect):
  params = Params(
    "PEST", [Insect.params],
    count = 300,
    move_dist_m = 4,
    move_dist_s = 2,
    food_cap = 240,
    food_m = 160,
    food_s = 40,
    foodsize = 36,
    feedtime = 16,
    feedchance = 0.4,
    repro_food = 100,
    repro_req = 120,
    reprorate = 0.04,
    deathrate = 0.0005,
  )

  def __init__(self, pos: Point):
    super().__init__(pos, (0xFF0000, 0xFF8000))

  def feed(self):
    Entity.log(self, "feed")

  def can_feed(self) -> bool:
    return True
