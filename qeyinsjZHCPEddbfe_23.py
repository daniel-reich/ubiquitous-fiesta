
def dice_game(lst):
  sum=0
  for i in range(len(lst)):
    if lst[i][0]==lst[i][1]:
      return 0
    else:
      sum+=lst[i][0]+lst[i][1]
  return sum

