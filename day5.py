from aoc import *

class DayFive:

  seatList = []
  ticketIds = []

  def __init__(self, file):
    self.seatList = file.copy()
    
  def partOne(self):
    for line in self.seatList:
      self.ticketIds.append(binaryPass(["R", "B"], line))
    self.ticketIds.sort()
    return self.ticketIds[-1]

  def partTwo(self):
    for i in range(len(self.ticketIds)):
      if self.ticketIds[i+1] == self.ticketIds[i]+2:
        return self.ticketIds[i]+1