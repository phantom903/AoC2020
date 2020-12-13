from aoc import *
from math import ceil

class DayThirteen:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    buses = ints(self.mem[1])
    myTime = int(self.mem[0])
    mods = dict()
    for bus in buses:
      mods[bus * ceil(myTime/bus)] = bus
    busId = mods[min(mods)]
    arrTime = min(mods)
    waitTime = arrTime - myTime
    return waitTime * busId

  def partTwo(self):
    buses = [[i, int(x)] for i, x in enumerate(self.mem[1].split(',')) if x != 'x']
    period = 1
    time = 0
    for position, bus in buses:
      found = False
      while not found:
        if (time + position) % bus == 0:
          found = True
        else:
          time += period
      period *= bus
    return time