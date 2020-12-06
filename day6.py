from aoc import *

class DaySix:
  
  ansList = []

  def __init__(self, ansList):
    self.ansList = ansList

  def partOne(self):
    results = []
    for passGroup in self.ansList:
      passGroup = ''.join(passGroup.split())
      answers = stripDups(passGroup)
      results.append(len(answers))
    return sum(results)

  def partTwo(self):
    results = []
    for passGroup in self.ansList:
      passGroup = passGroup.split()
      answers = showDups(passGroup)
      results.append(len(answers))
    return sum(results)