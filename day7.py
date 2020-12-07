from aoc import *
# from queue import Queue

# def parseBagRule(bagRule):
#   if len(bagRule.split(' ')) == 3:
#     amount = 1
#     bagColour = "".join(bagRule.split(' ')[0:2])
#   else:
#     amount = ints(bagRule)[0]
#     bagColour = "".join(bagRule.split(' ')[1:3])
#   return {'colour': bagColour, 'amount': amount}

# def parseBagList(bagList):
#   bagRules = {}
#   for bagRule in bagList:
#     containerStr, contentStr = bagRule.split(' contain ')
#     rules = []
#     for bag in contentStr.split(', '):
#       rules.append(parseBagRule(bag))
#     container = parseBagRule(containerStr)
#     bagRules[container['colour']] = {'contents': rules}
#   return bagRules
  
# credit to reddit user Jai_Wicked11
# https://github.com/VitaminJai/AOC2020/blob/main/Day7/day7.1.py
# significantly simpler solution than i was attempting
def findBags(bags, stringNeeded):
  bagsList = []
  for bag in bags:
    findBag = bag.find(' bags contain')
    if stringNeeded in bag[findBag:]:
      bagsList.append(bag[:findBag])
      bagsList.extend(findBags(bags, bag[:findBag]))
  return bagsList

def getBag(bags, stringNeeded):
  total = 1
  if 'no other' in bags[stringNeeded]:
    return 1
  for colours in bags[stringNeeded]:
    each = colours.split()
    total += int(each[0]) * getBag(bags, ' '.join(each[1:]))
  return total -1

class DaySeven:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    # bagRules = parseBagList(self.mem)
    # result = 0
    # for line in bagRules.keys():
    #   if line != 'shinygold':
    #     rules = Queue()
    #     for i in bagRules[line]['contents']:
    #       rules.put(i['colour'])
    #       while not rules.empty
    bagsList = set(findBags(self.mem, "shiny gold"))
    return len(bagsList)

  def partTwo(self):
    allBags = {}
    for line in self.mem:
      line = line.replace('bags', '').replace('bag', '').strip('.')
      line = line.split('contain')
      allBags[line[0].strip()] = line[1].strip().split(',')
    return getBag(allBags, 'shiny gold')


