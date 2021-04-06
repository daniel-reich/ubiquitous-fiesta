
def dice_game(lst):
  total = 0
  for roll in lst:
    if roll[0] == roll[1]:
      return 0
    else:
      total += sum(roll)
  return total

