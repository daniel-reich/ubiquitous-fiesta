
def dice_game(lst):
  return sum(a+b for a, b in lst) if not any(a==b for a, b in lst) else 0

