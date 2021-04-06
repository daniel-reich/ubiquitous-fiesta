
def dice_game(lst):
  result = [0 if x == y else x + y for x, y in lst]
  if 0 in result:
    return 0
  else:
    return sum(result)

