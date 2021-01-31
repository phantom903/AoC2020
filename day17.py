from aoc import *
from itertools import product
from copy import deepcopy

class DaySeventeen:

  mem = []
  map3d = []
  dimension = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.map3d = [[['.' for x in range(len(mem[0]))] for y in range(len(mem)) for z in (-1,0-1)]]
    for y in range(len(self.mem)):
      for x in range(len(self.mem[0])):
        if self.mem[y][x] == '#':
          self.dimension.append((x,y,0))
          self.map3d[0][y][x] = '#'
        else:
          self.map3d[0][y][x] = '.'

  def getNeighbours(self, x, y, z):
    return sum((x + _x, y + _y, z + _z) in self.dimension for _x, _y, _z in product((-1, 0, 1), repeat=3)) - ((x, y, z) in self.dimension)

  def iterateCubes(self, runs):
    for i in range(1, runs+1):
      dimension = deepcopy(self.dimension)
      for y in range(0-i,len(self.mem)+i,1):
        for x in range(0-i,len(self.mem[0])+i,1):
          for z in range(-i, i, 1):
            if self.getNeighbours(x,y,z) not in (2, 3) and (x, y, z) in dimension:
              dimension.remove((x, y, z))
              self.map3d[z][y][x] = '.'
            elif (x, y, z) not in dimension and self.getNeighbours(x, y, z) == 3:
              dimension.append((x, y, z))
              self.map3d[z][y][x] = '#'
      self.dimension = deepcopy(dimension)

  def partOne(self):
    self.iterateCubes(6)
    print(self.map3d)
    return (len(self.dimension))

  def partTwo(self):
    pass