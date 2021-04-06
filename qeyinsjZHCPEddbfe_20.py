
def dice_game(lst):
  if any(len(set(t)) == 1 for t in lst): return 0
  return sum(sum(t) for t in lst)

