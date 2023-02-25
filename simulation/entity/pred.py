from .insect import Insect
from .params import Params
from ..util import Point

class Pred(Insect):
  params = Params(
    "PRED", [Insect.params],
    foodtype = "PEST",
    count = 80,
    move = 0.8,
    move_dist_m = 8,
    move_dist_s = 4,
    move_idle = 0.3,
    food_cap = 400,
    food_m = 240,
    food_s = 80,
    foodsize = 50,
    food_search = 0.8,
    foodattr = (40, 20),
    feedtime = 24,
    repro_food = 100,
    repro_req = 150,
    reprorate = 0.005,
  )

  def __init__(self, pos: Point):
    super().__init__(pos, (0x00FF00, 0xFFFF00))
