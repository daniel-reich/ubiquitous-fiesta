
direction = { "N": 1, "S": -1, "E": 2, "W": -2, }
​
def back_to_home(d):
  return sum([direction[i] for i in d]) == 0

