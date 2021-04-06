
def dice_game(lst):
  score = 0
  for roll in lst:
    if roll[0] == roll[1]:
      return 0
    score = score + roll[0] + roll[1]
  return score

