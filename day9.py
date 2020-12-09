from aoc import *

class InValidNum(Exception):
  pass

def isSum(numList, target):
  for i in range(len(numList)):
    if (target - numList[i]) in numList:
      return True
  return False

def findMultiSum(numList, target):
  runList = []
  for i in range(len(numList)):
    thisList = numList[i:].copy()
    for j in range(len(thisList)):
      runList.append(thisList[j])
      if (target == sum(runList)) and (len(runList) > 1):
        return runList
      elif target < sum(runList):
        runList.clear()

def parseXMAS(mem, preamble):
  for i in range(preamble, len(mem)):
    if not isSum(mem[i-preamble:i], mem[i]):
      raise InValidNum(mem[i])


class DayNine:

  mem = []
  testMem = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    try:
      parseXMAS(self.mem, 25)
    except InValidNum as e:
      return str(e)

  def partTwo(self):
    result = findMultiSum(self.mem, int(self.partOne()))
    return min(result) + max(result)