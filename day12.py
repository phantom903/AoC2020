from aoc import *

class DayTwelve:

  mem = []
  position = {'N':0, 'E':0, 'S':0, 'W':0}
  directions = {0: 'N', 90:'E', 180:'S', 270:'W'}
  facing = 90
  waypoint = {'N':1, 'E':10, 'S':0, 'W':0}

  def __init__(self, mem):
    for i in range(len(mem)):
      self.mem.append((mem[i][0], ints(mem[i])[0]))

  def move(self, instr):
    op, arg = instr[0], instr[1]
    if op not in ('R','L','F'):
      self.position[op] += arg
    elif op == 'R':
      self.facing += arg
      if self.facing >= 360:
        self.facing -= 360
    elif op == 'L':
      self.facing -= arg
      if self.facing < 0:
        self.facing += 360
    elif op == 'F':
      self.position[self.directions[self.facing]] += arg

  def rotateWaypoint(self, dir):
    dirs = {0:'N', 1:'E', 2:'S', 3:'W'}
    ops = {'R': 1, 'L': -1}
    oldNorth = self.waypoint['N']
    if dir == 'R':
      self.waypoint['N'] = self.waypoint['W']
      self.waypoint['W'] = self.waypoint['S']
      self.waypoint['S'] = self.waypoint['E']
      self.waypoint['E'] = oldNorth
    elif dir == 'L':
      self.waypoint['N'] = self.waypoint['E']
      self.waypoint['E'] = self.waypoint['S']
      self.waypoint['S'] = self.waypoint['W']
      self.waypoint['W'] = oldNorth
      
  def moveWaypoint(self, instr):
    op, arg = instr[0], instr[1]
    if op in ('N', 'E', 'S', 'W'):
      self.waypoint[op] += arg
    elif op in ('R', 'L'):
      for i in range(int(arg/90)):
        self.rotateWaypoint(op)

  def partOne(self):
    for i in self.mem:
      self.move(i)
    horiz = abs(self.position['W'] - self.position['E'])
    vert = abs(self.position['S'] - self.position['N'])
    return horiz+vert

  def partTwo(self):
    dirs = ('N', 'E', 'S', 'W')
    for i in dirs:
      self.position[i] = 0
    for i in self.mem:
      op, arg = i[0], i[1]
      if op == 'F':
        for x in dirs:
          self.position[x] += (self.waypoint[x] * arg)
      else:
        self.moveWaypoint(i)

    horiz = abs(self.position['W'] - self.position['E'])
    vert = abs(self.position['S'] - self.position['N'])
    return horiz+vert
