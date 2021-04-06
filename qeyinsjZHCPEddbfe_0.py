
def dice_game(lst):
  score = 0
  for a, b in lst:
    if a == b:
      return 0
    score += a+b
  return score

