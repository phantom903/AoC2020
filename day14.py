from aoc import *
from collections import defaultdict
from itertools import product

class DayFourteen:

  prog = []
  mem = {}
  mask = ''

  def __init__(self, mem):
    self.prog = mem.copy()
    self.memInit()

  def setMask(self, newMask):
    self.mask = newMask.split(' = ')[1]

  def memInit(self):
    self.mem = defaultdict(lambda: 0)

  def convertVal(self, data):
    result = ''
    for i in range(len(data)):
      result += data[i] if self.mask[i] == 'X' else self.mask[i]
    return result

  def combinations(self, data):
    seq = list(data)
    indices = [i for i, c in enumerate(seq) if c == 'X']
    for perm in product('01', repeat=len(indices)):
      for i, c in zip(indices, perm):
        seq[i] = c
      yield ''.join(seq)

  def convertAddrs(self, data):
    result = []
    location = ''
    memLoc = format(data, '036b')
    for i in range(len(memLoc)):
      location += memLoc[i] if self.mask[i] == '0' else self.mask[i]
    return list(self.combinations(location))

  def storeVal(self, memLoc, val):
    self.mem[memLoc] = int(val, 2)

  def partOne(self):
    for line in self.prog:
      if 'mask' in line:
        self.setMask(line)
      else:
        memLoc, val = line.split(' = ')
        memLoc = ints(memLoc)[0]
        val = self.convertVal(format(int(val), '036b'))
        self.storeVal(memLoc, val)
    return sum(self.mem.values())

  def partTwo(self):
    memLocs = []
    self.memInit()
    for line in self.prog:
      if 'mask' in line:
        self.setMask(line)
      else:
        memLoc, val = line.split(' = ')
        memLoc = ints(memLoc)[0]
        memLocs = self.convertAddrs(memLoc)
        for i in memLocs:
          self.storeVal(i, format(int(val), '036b'))
    return sum(self.mem.values())