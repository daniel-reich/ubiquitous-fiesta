
def dice_game(lst):
  return 0 if any([a == b for a, b in lst]) else sum([a + b for a, b in lst])

