from day6 import DaySix
from day1 import DayOne
from day2 import DayTwo
from day3 import DayThree
from day4 import DayFour
from aoc import fileOpenLines, fileOpenNewLines, ints
import sys

from day5 import DayFive
from day7 import DaySeven

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
  print("Part 1: ", daySeven.partOne())
  print("Part 2: ", daySeven.partTwo())