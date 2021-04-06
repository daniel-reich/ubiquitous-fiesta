
def dice_game(lst):
  for i in lst: 
    if i[0]==i[1]: return 0
  return sum(sum(i) for i in lst)

