from aoc import *
import re

class DayFour:

  subStrings = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  validPassports = []

  def partOne(self, passFile):
    result = 0
    for line in passFile:
      if all([subString in line for subString in self.subStrings]):
        result += 1
        self.validPassports.append(line)
    return result

  def partTwo(self):
    result = 0
    for passport in self.validPassports:
      tokens = []
      eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
      pairs = passport.split(' ')
      for pair in pairs:
        tokens.append(pair.split(':'))
      for token in tokens:
        token.append(False)
        if any([
          ((token[0] == "byr") and (int(token[1]) >= 1920) and (int(token[1]) <= 2002)),
          ((token[0] == "iyr") and (int(token[1]) >= 2010) and (int(token[1]) <= 2020)),
          ((token[0] == "eyr") and (int(token[1]) >= 2020) and (int(token[1]) <= 2030)),
          ((token[0] == "hgt") and ("in" in token[1]) and (int(ints(token[1])[0]) >= 59) and (int(ints(token[1])[0]) <= 76)),
          ((token[0] == "hgt") and ("cm" in token[1]) and (int(ints(token[1])[0]) >= 150) and (int(ints(token[1])[0]) <= 193)),
          ((token[0] == "hcl") and (re.match('^#[a-f0-9]{6}$', token[1]) is not None)),
          ((token[0] == "ecl") and (token[1] in eyes)),
          ((token[0] == "pid") and (re.match("^[0-9]{9}$", token[1]) is not None)),
          (token[0] == "cid")
        ]):
          token[2] = True
      if all(token[2] for token in tokens):
        result += 1
    return result
