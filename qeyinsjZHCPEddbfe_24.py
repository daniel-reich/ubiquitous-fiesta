
def dice_game(lst):
  total = 0
  for x in lst:
    if x[0]==x[1]:
      total = 0
      break
    else:
      total += sum(x)
  print (total)
  return total

