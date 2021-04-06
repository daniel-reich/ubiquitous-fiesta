
def dice_game(lst):
  return sum([sum(x) for x in lst]) if all([True if len(set(z))==len(z) else False for z in lst]) else 0

