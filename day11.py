from aoc import *
from copy import deepcopy

class DayEleven:

  mem = []

  def __init__(self, mem):
    self.mem = deepcopy(mem)
    for i in range(len(self.mem)):
      self.mem[i] = ['#' if j == 'L' else '.' for j in self.mem[i]]

  def checkAdj(self, data, xy):
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    maxX = len(data[0])
    maxY = len(data)
    count = 0
    for x, y in dirs:
      if (0 <= (xy[0]+x) < maxX) and (0 <= (xy[1]+y) < maxY):
        if data[xy[1]+ y][xy[0] + x] == '#':
          count += 1
    return count

  def changeMap(self, origMap):
    changes = 0
    newMem = deepcopy(origMap)
    for y in range(len(origMap)):
      for x in range(len(origMap[0])):
        adjSeats = self.checkAdj(origMap, [x,y])
        curSeat = origMap[y][x]
        if curSeat == '#' and adjSeats >= 4:
            newMem[y][x] = 'L'
            changes += 1
        elif curSeat == 'L' and adjSeats == 0:
            newMem[y][x] = '#'
            changes =+ 1
    return deepcopy(newMem), changes

  def partOne(self):
    changes = 1
    p1map = deepcopy(self.mem)
    result = 0
    while changes != 0:
      p1map, changes = self.changeMap(p1map) 
    for y in range(len(p1map)):
      for x in range(len(p1map[0])):
        result += 1 if p1map[y][x] == '#' else 0
    return result 

  def partTwo(self):
    pass