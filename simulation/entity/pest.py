from entity.base import Entity
from entity.insect import Insect
from entity.params import Params
from util import Point

class Pest(Insect):
  params = Params(
    "PEST", [Insect.params],
    count = 300,
    food_cap = 100,
    food_m = 60,
    food_s = 20,
    foodsize = 20,
    feedtime = 2,
    feedchance = 0.2,
    repro_food = 40,
    repro_req = 50,
    reprorate = 0.02,
    deathrate = 0.0005,
  )

  def __init__(self, pos: Point):
    super().__init__(Pest.params, pos, (0xFF0000, 0xFF8000))

  def feed(self) -> None:
    Entity.log(self, "feed")

  def can_feed(self) -> bool:
    return True
