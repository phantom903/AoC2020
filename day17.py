from aoc import *
from itertools import product
from copy import deepcopy

class DaySeventeen:

  mem = []
  dimension = []

  def __init__(self, mem):
    self.mem = mem.copy()
    for y in range(len(self.mem)):
      for x in range(len(self.mem[0])):
        if self.mem[y][x] == '#':
          self.dimension.append((x,y,0))

  def getNeighbours(self, x, y, z):
    return sum((x + _x, y + _y, z + _z) in self.dimension for _x, _y, _z in product((-1, 0, 1), repeat=3)) - ((x, y, z) in self.dimension)

  def iterateCubes(self, runs):
    for i in range(runs):
      dimension = deepcopy(self.dimension)
      for cube in dimension:
        x, y, z = cube[0], cube[1], cube[2]
        if self.getNeighbours(x,y,z) not in (2, 3) and (x, y, z) in dimension:
          dimension.remove((x, y, z))
        elif (x, y, z) not in dimension and self.getNeighbours(x, y, z) == 3:
          dimension.append((x, y, z))
      self.dimension = deepcopy(dimension)

  def partOne(self):
    self.iterateCubes(6)
    return len(self.dimension)

  def partTwo(self):
    pass