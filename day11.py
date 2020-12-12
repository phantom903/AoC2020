from aoc import *
from copy import deepcopy

# ~6.02s with [list] of [list]s
# ~3.87s with sets

class DayEleven:

  mem = []
  emptySeats = set()
  fullSeats = set()
  rows = 0
  cols = 0

  def __init__(self, mem):
    self.mem = mem.copy()
    self.rows = len(mem)
    self.cols = len(mem[0])
    for y in range(self.rows):
      for x in range(self.cols):
        if self.mem[y][x] == 'L':
          self.fullSeats.add((x,y))
  
  def visibleSeats(self, seatType, changesE, changesF, dirs, xy):
    count = 0
    for x, y in dirs:
      pos = (x+xy[0],y+xy[1])
      if seatType == 'full':
        if ((pos in self.fullSeats) or (pos in changesE)) and (pos not in changesF):
          count += 1
    return count

  def checkDir(self, dir, changesE, changesF, xy):
    i = 1
    while 0 <= i <= max(self.rows, self.cols):
      pos = ((dir[0]*i)+xy[0], (dir[1]*i)+xy[1])    
      if ((pos in self.fullSeats) or (pos in changesE)) and (pos not in changesF):
        return 1
      elif ((pos in self.emptySeats) or (pos in changesF)) and (pos not in changesE):
        return 0
      else:
        i += 1
    return 0
  
  def checkAdj(self, changesE, changesF, xy, los):
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    count = 0
    if not los:
      return self.visibleSeats('full', changesE, changesF, dirs, xy)
    else:
      for i in dirs:
        count += self.checkDir(i, changesE, changesF, xy)
      return count

  def changeMap(self, tolerance, los):
    changesE = set()
    changesF = set()
    for y in range(self.rows):
      for x in range(self.cols):
        adjSeats = self.checkAdj(changesE, changesF, [x,y], los)
        if adjSeats >= tolerance and (x,y) in self.fullSeats:
          self.emptySeats.add((x,y))
          self.fullSeats.remove((x,y))
          changesE.add((x,y))
        elif adjSeats == 0 and (x,y) in self.emptySeats:
          self.emptySeats.remove((x,y))
          self.fullSeats.add((x,y))
          changesF.add((x,y))
    return len(changesE)+len(changesF)

  def partOne(self):
    changes = 1
    result = 0
    while changes != 0:
      changes = self.changeMap(4, False)
    result = len(self.fullSeats)
    return result 

  def partTwo(self):
    # changes = 1
    # result = 0
    # while changes != 0:
    #   changes = self.changeMap(5, True)
    # result = len(self.fullSeats)
    print(self.checkAdj({}, {}, (0,0), True))
    # return result