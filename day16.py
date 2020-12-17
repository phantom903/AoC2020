from aoc import *
from copy import deepcopy

class DaySixteen:

  rules = []
  rulesMem = []
  tickets = []

  def __init__(self, mem):
    tempMem = []
    for line in mem:
      if not line in ('', None, '\n\n'):
          if 'your' in line:
            self.rulesMem = deepcopy(tempMem)
            tempMem.clear()
          elif 'nearby' in line:
            self.myTicket = deepcopy(tempMem)
            tempMem.clear()
          else:
            tempMem.append(line)
    self.tickets = deepcopy(tempMem)
    

  def parseRules(self):
    i = 0
    done = False
    low = []
    hi = []
    for i in range(len(self.rulesMem )):
      line = self.rulesMem[i]
      line = line.split(': ')
      ranges = line[1].replace(' or ', '-').split('-')
      [low.append(i) for i in range(int(ranges[0]), int(ranges[1])+1)]
      [hi.append(i) for i in range(int(ranges[2]), int(ranges[3])+1)]
    return low, hi
        
  def partOne(self):
    inValids = 0
    low, hi = self.parseRules()
    for ticket in self.tickets:
      invalidTicket =False
      for i in ints(ticket):
        if not i in low and not i in hi:
          inValids += i
          invalidTicket = True
    return inValids

  def partTwo(self):
    low, hi = self.parseRules()
    for ticket in self.tickets:
      invalidTicket =False
      for i in ints(ticket):
        if not i in low and not i in hi:
          invalidTicket = True
      if invalidTicket:
        self.tickets.remove(ticket)
    