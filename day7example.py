from aoc import openFileLines
from collections import defaultdict
from math import ceil
from queue import Queue

n = openFileLines('14')

def parseIngredient(recipe):
  parts = recipe.split(' ')
  return {'ingredient': parts[1], 'amount': int(parts[0])}

def parseRecipes(data):
  recipes = {}
  for line in data:
    inputStr, outputStr = line.split(' => ')
    ingredients = []
    for ingredient in inputStr.split(', '):
      ingredients.append(parseIngredient(ingredient))
    output = parseIngredient(outputStr)
    recipes[output['ingredient']] = {'servings': output['amount'], 'ingredients': ingredients}
  return recipes

def makeFuel(amount, recipes):
  supply = defaultdict(int)
  orders = Queue()
  orders.put({'ingredient': 'FUEL', 'amount': amount})
  oreNeeded = 0

  while not orders.empty():
    order = orders.get()
    if order['ingredient'] == 'ORE':
      oreNeeded += order['amount']
    elif order['amount'] <= supply[order['ingredient']]:
      supply[order['ingredient']] -= order['amount']
    else:
      amountNeeded = order['amount'] - supply[order['ingredient']]
      recipe = recipes[order['ingredient']]
      batches = ceil(amountNeeded / recipe['servings'])
      for ingredient in recipe['ingredients']:
        orders.put({'ingredient': ingredient['ingredient'], 'amount': ingredient['amount'] * batches})
        leftoverAmount = batches * recipe['servings'] - amountNeeded
        supply[order['ingredient']] = leftoverAmount
  return oreNeeded

data = [row.strip() for row in n]
recipes = parseRecipes(data)
orePerFuel = makeFuel(1, recipes)
print('Part 1: ', orePerFuel)

upperBound = None
lowerBound = 1
oreCapacity = 1000000000000
while lowerBound + 1 != upperBound:
  if upperBound is None:
    guess = lowerBound * 2
  else: guess = (upperBound + lowerBound) // 2

  oreNeeded = makeFuel(guess, recipes)
  if oreNeeded > oreCapacity:
    upperBound = guess
  else:
    lowerBound = guess

print('Part 2: ', lowerBound)
