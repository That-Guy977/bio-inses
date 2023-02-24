from .insect import Insect
from .params import Params
from ..util import Point

class Pred(Insect):
  params = Params(
    "PRED", [Insect.params],
    foodtype = "PEST",
    count = 80,
    move = 0.8,
    move_dist_m = 20,
    move_dist_s = 12,
    move_idle = 0.3,
    food_cap = 200,
    food_m = 80,
    food_s = 40,
    foodsize = 30,
    food_search = 0.8,
    foodattr = (40, 15),
    feedtime = 8,
    repro_food = 40,
    repro_req = 100,
    reprorate = 0.008,
  )

  def __init__(self, pos: Point):
    super().__init__(Pred.params, pos, (0x00FF00, 0xFFFF00))
