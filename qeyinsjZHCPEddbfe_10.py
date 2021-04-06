
def dice_game(lst):
  for x in lst:
    if x[0] == x[1]:
      return 0    
  return sum(x[0] + x[1] for x in lst)

