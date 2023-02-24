from __future__ import annotations
from ..util import deviate

class Params:
  def __init__(self, type: str, parents: list[Params] = [], **kwargs):
    self.type = type
    self.parents = { parent.type for parent in parents }
    for k in kwargs:
      self[k] = kwargs[k]
    for parent in parents:
      for k in parent:
        if k not in self:
          self[k] = parent[k]

  def generate(self, param: str) -> int:
    return deviate(self[param + "_m"], self[param + "_s"])

  def __contains__(self, name: str):
    return hasattr(self, name)

  def __iter__(self):
    for k in vars(self):
      yield k

  def __getitem__(self, name: str):
    return getattr(self, name)

  def __setitem__(self, name: str, value):
    setattr(self, name, value)
