from aoc import *

class DayFifteen:

  mem = []
  played = dict()
  turns = dict()

  def __init__(self, mem):
    self.mem = mem.copy()
    for i in range(len(mem)):
      self.played[mem[i]] = [i + 1]
      self.turns[i + 1] = mem[i]

  def memClear(self):
    self.played.clear()
    self.turns.clear()
    for i in range(len(self.mem)):
      self.played[self.mem[i]] = [i + 1]
      self.turns[i + 1] = self.mem[i]

  def playGame(self, runs):
    for i in range(len(self.played) + 1, runs + 1, 1):
      if len(self.played[self.turns[i-1]]) == 1:
        self.turns[i] = 0
        self.played[0] += [i]
      else:
        turnDiff = self.played[self.turns[i-1]][-1] - self.played[self.turns[i-1]][-2]
        self.turns[i] = turnDiff
        if turnDiff in self.played.keys():
          self.played[turnDiff] += [i]
        else:
          self.played[turnDiff] = [i]
    return self.turns[runs]

  def betterGame(self, runs):
    self.memClear()
    lastNumber = self.mem[-1]
    for i in range(len(self.mem), runs, 1):
      pass

  def partOne(self):
    return self.playGame(2020)

  def partTwo(self):
    self.memClear()
    return self.playGame(30000000)