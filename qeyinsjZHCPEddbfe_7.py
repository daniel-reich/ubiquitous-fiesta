
def dice_game(lst):
  total = 0
  
  for string in lst:
    check = []
    for value in string:
      if value in check:
        return 0
      else:
        check.append(value)
        total += value
  return total

