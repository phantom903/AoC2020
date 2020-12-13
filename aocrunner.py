from day6 import DaySix
from day1 import DayOne
from day2 import DayTwo
from day3 import DayThree
from day4 import DayFour
from aoc import fileOpenLines, fileOpenNewLines, ints
import sys
import time
from day5 import DayFive
from day7 import DaySeven
from day8 import DayEight
from day9 import DayNine
from day10 import DayTen
from day11 import DayEleven
from day12 import DayTwelve
from day13 import DayThirteen

if len(sys.argv) > 1:
  dayChoice = sys.argv[1]
else:
  dayChoice = input("Which day?: ")
if dayChoice == "1":
  y = fileOpenLines(1, "i")
  dayOne = DayOne()
  print("Part 1: " , dayOne.partOne(y))
  print("Part 2: " , dayOne.partTwo(y))
elif dayChoice == "2":
  y = fileOpenLines(2, "s")
  dayTwo = DayTwo()
  print("Part 1: " , dayTwo.partOne(y))
  print("Part 2: " , dayTwo.partTwo(y))
elif dayChoice == "3":
  y = fileOpenLines(3, "s")
  dayThree = DayThree()
  print("Part 1: " , dayThree.pathCalc(y, 1))
  print("Part 2: " , dayThree.pathCalc(y, 2))
elif dayChoice == "4":
  y = fileOpenNewLines(4)
  dayFour = DayFour()
  print("Part 1: ", dayFour.partOne(y))
  print("Part 2: ", dayFour.partTwo())
elif dayChoice == "5":
  y = fileOpenLines(5, "s")
  dayFive = DayFive(y)
  print("Part 1: ", dayFive.partOne())
  print("Part 2: ", dayFive.partTwo())
elif dayChoice == "6":
  y = fileOpenNewLines(6)
  daySix = DaySix(y)
  print("Part 1: ", daySix.partOne())
  print("Part 2: ", daySix.partTwo())
elif dayChoice == "7":
  y = fileOpenLines(7,"s")
  daySeven = DaySeven(y)
  print("Still to solve myself")
  # print("Part 1: ", daySeven.partOne())
  # print("Part 2: ", daySeven.partTwo())
elif dayChoice == "8":
  y = fileOpenLines(8,"s")
  dayEight = DayEight(y)
  print("Part 1: ", dayEight.partOne())
  print("Part 2: ", dayEight.partTwo())
elif dayChoice == "9":
  y = fileOpenLines(9,"i")
  dayNine = DayNine(y)
  print("Part 1: ", dayNine.partOne())
  print("Part 2: ", dayNine.partTwo())
elif dayChoice == "10":
  y = fileOpenLines(10,"i")
  dayTen = DayTen(y)
  print("Part 1: ", dayTen.partOne())
  print("Part 2: ", dayTen.partTwo(max(y)))
elif dayChoice == "11":
  y = fileOpenLines('11a',"s")
  dayEleven = DayEleven(y)
  startTime = time.time()
  print("Part 1: ", dayEleven.partOne(), " in ", round(time.time() - startTime,2), "s")
  startTime = time.time()
  print("Part 2: ", dayEleven.partTwo(), " in ", round(time.time() - startTime, 2), "s")
elif dayChoice == "12":
  y = fileOpenLines(12,"s")
  dayTwelve = DayTwelve(y)
  startTime = time.time()
  print("Part 1: ", dayTwelve.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwelve.partTwo(), " in ", round(time.time() - startTime, 2), "s")
elif dayChoice == "13":
  y = fileOpenLines(13,"s")
  dayThirteen = DayThirteen(y)
  startTime = time.time()
  print("Part 1: ", dayThirteen.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayThirteen.partTwo(), " in ", round(time.time() - startTime, 2), "s")