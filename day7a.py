inputs = open('input/day7.txt', "r").read().splitlines()
def find_child_bags(bag):
  for input in inputs:
    start,end = input.replace(".","").replace(" ","").split("contain")
    if bag.replace(" ", "") in start:
      if "noother" in end:
        return 1
      total = 0
      for b in end.split(","):
        total += int(b[0]) * find_child_bags(b[1:])
      return total + 1
print(find_child_bags("shiny gold")-1)

#Not my solution - still to have a crack at this one
#https://www.reddit.com/r/adventofcode/comments/k8a31f/2020_day_07_solutions/gezq40d?utm_source=share&utm_medium=web2x&context=3