from __future__ import annotations
import random
from .base import Entity
from .pos import Position
from .params import Params
from ..util import Point, deviate
from typing import Sequence

class Insect(Entity):
  params = Params(
    "INSC",
    size = 6,
    count = 100,
    move = 0.8,
    move_dist_m = 18,
    move_dist_s = 15,
    move_idle = 0.8,
    move_rand = 5,
    foodtype = [],
    feedchance = 1.0,
    trapattr = (10, 5),
    reprorate = 0.005,
    deathrate = 0.002,
  )

  counts: dict[str, int] = {}

  def __init__(self, pos: Point, colors: tuple[int, int]):
    super().__init__(pos, colors[0])
    self.state = InsectState(self)
    self.colors = colors
    if self.type not in Insect.counts:
      Insect.counts[self.type] = 0
    Insect.counts[self.type] += 1
    Entity.log(self, "init")

  def update(self):
    if not self.state.active:
      return super().kill()
    self.state.update()
    super().update()

  def move(self):
    target = self.state.target
    dist = self.params.generate("move_dist")
    theta = deviate(self.pos.direction(target.pos), self.params.move_rand)
    if target.type == "POS":
      if random.random() >= self.params.move_idle:
        return
    target_dist = self.pos.distance_to(target.pos)
    if target_dist < dist:
      dist = target_dist
    self.pos += Point.polar(dist, theta)
    Entity.log(self, "move", target)

  def search(self): 
    target = self.state.target
    attr = self.get_attr(target) if target is not None else 0
    for entity in self.groups()[0]:
      ent_attr = self.get_attr(entity)
      if ent_attr > attr and ent_attr >= 0.5:
        target = entity
        attr = ent_attr
    if target is None:
      target = Position(Point.random())
    elif attr < 1:
      target = Position(target.pos)
    if target != self.state.target:
      Entity.log(self, "trgt", target)
    self.state.target = target

  def feed(self):
    self.eat(self.state.target)
    self.state.target = None

  def eat(self, target: Entity):
    target.kill()
    Entity.log(self, "eat", target)

  def repro(self):
    child = self.copy(self)
    for group in self.groups():
      group.add(child)
    Entity.log(self, "repr")

  def kill(self):
    if self.state.active:
      self.remove()
      Insect.counts[self.type] -= 1
      Entity.log(self, "dead")

  def mark(self):
    self.state.reset()
    self.state.mark = True
    self.color(self.colors[1])
    Entity.log(self, "mark")

  def remove(self):
    self.state.active = False

  def can_feed(self) -> bool:
    return self.state.target.type == self.params.foodtype \
    and self.state.target.state.active \
    and self.touch(self.state.target)

  def get_attr(self, target: Entity) -> float:
    dist = self.pos.distance_to(target.pos)
    attr_str = None
    if target.type == "TRAP":
      attr_str = self.params.trapattr
    elif target.type in self.params.foodtype:
      search_threshold = self.params.food_cap * self.params.food_search
      if self.state.food <= search_threshold:
        attr_str = self.params.foodattr
    return 2**((attr_str[0]-dist)/attr_str[1]) if attr_str else 0.0

  @classmethod
  def copy(cls, src):
    return cls(src.pos)

  @classmethod
  def generate(cls):
    return [cls(Point.random()) for _ in range(cls.params.count)]

class InsectState:
  def __init__(self, insect: Insect):
    self.insect = insect
    self.reset()

  def update(self):
    self.insect.search()
    params = self.insect.params
    if self.feed > 0:
      self.feed -= 1
      return
    if random.random() < params.move:
      self.insect.move()
    self.food -= 1
    if self.food == 0 or random.random() < params.deathrate:
      Entity.log(self.insect, "strv")
      self.insect.kill()
      return
    if self.food >= params.repro_req and random.random() < params.reprorate:
      self.insect.repro()
      self.food -= params.repro_food
    if self.insect.can_feed() and random.random() < params.feedchance:
      self.feed = params.feedtime
      self.insect.feed()
      self.food = min(self.food + params.foodsize, params.food_cap)

  def reset(self):
    self.food = self.insect.params.generate("food")
    self.feed = 0
    target: Entity = None
    self.target = target
    self.active = True
    self.mark = False
