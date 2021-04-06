
def dice_game(lst):
  total = 0
  for i in lst:
    if i[0] == i[1]:
      return 0
    else:
      total += i[0] + i[1]
  return total

