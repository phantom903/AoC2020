from aoc import *
from functools import lru_cache

class DayTen:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    adapters = [0]
    ones = 0
    threes = 0
    for i in self.mem:
      adapters.append(i)
    adapters.append(max(adapters)+3)
    adapters.sort()
    for i in range(1, len(adapters)):
      if adapters[i] - adapters[i-1] == 3:
        threes += 1
      elif adapters[i] - adapters[i-1] == 1:
        ones += 1
    self.mem.clear()
    self.mem = adapters.copy()
    return ones * threes

  @lru_cache()
  def partTwo(self, tgt):
    if tgt == 0:
      return 1
    if tgt not in self.mem:
      return 0
    else:
      return sum([self.partTwo(tgt-1), self.partTwo(tgt-2), self.partTwo(tgt-3)])
    