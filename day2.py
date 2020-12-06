from aoc import ints

class DayTwo():

  def partOne(self, pwdSet):
    solutions = 0
    pwdSetSplit = [pwdLine.split(":") for pwdLine in pwdSet]
    pwdTok = [pwdLine[0].split() for pwdLine in pwdSetSplit]
    pwdLines = [pwdLine[1] for pwdLine in pwdSetSplit]
    for i in range(len(pwdSet)):
      idxs = ints(pwdTok[i][0])
      startIdx = idxs[0]
      stopIdx = idxs[1]
      if pwdLines[i].count(pwdTok[i][1]) >= startIdx and pwdLines[i].count(pwdTok[i][1]) <= stopIdx:
        solutions += 1
    return solutions

  def partTwo(self, pwdSet):
    solutions = 0
    pwdSetSplit = [pwdLine.split(":") for pwdLine in pwdSet]
    pwdTok = [pwdLine[0].split() for pwdLine in pwdSetSplit]
    pwdLines = [pwdLine[1] for pwdLine in pwdSetSplit]
    for i in range(len(pwdSet)):
      idxs = ints(pwdTok[i][0])
      startIdx = idxs[0]
      stopIdx = idxs[1]
      if (pwdLines[i][startIdx] == pwdTok[i][1] and not pwdLines[i][stopIdx] == pwdTok[i][1]) or (pwdLines[i][stopIdx] == pwdTok[i][1] and not pwdLines[i][startIdx] == pwdTok[i][1]):
        solutions += 1
    return solutions