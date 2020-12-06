class DayOne():
  def partOne(self, inputStr):
    for i in inputStr:
      for j in inputStr:
        if i + j == 2020:
          return (i*j)

  def partTwo(self, inputStr):
    for i in inputStr:
      for j in inputStr:
        for k in inputStr:
          if i + j + k == 2020:
            return (i*j*k)

