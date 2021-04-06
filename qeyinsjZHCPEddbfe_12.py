
def dice_game(lst):
  counter = 0
  for i in lst:
    if i[0] == i[1]:
      return 0
    else:
      counter += sum(i)
  return counter

