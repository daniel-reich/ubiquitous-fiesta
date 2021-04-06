
def calculate_score(games):
  leftwin = 0
  rightwin = 0
  for i in games:
    if check(i) == "tie":
      leftwin += 1
      rightwin += 1
    elif check(i) == "left":
      leftwin += 1
    elif check(i) == "right":
      rightwin += 1
  if leftwin > rightwin:
    return "Abigail"
  elif rightwin > leftwin:
    return "Benson"
  else:
    return "Tie"
      
def check(lst):
  if lst[0] == lst[1]:
    return "tie"
  elif lst[0] == "R" and lst[1] == "P":
    return "right"
  elif lst[0] == "P" and lst[1] == "S":
    return "right"
  elif lst[0] == "S" and lst[1] == "R":
    return "right"
  else:
    return "left"

