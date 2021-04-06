
def dice_game(lst):
  res = 0
  for i in lst:
    if i[0]==i[1]: return 0
    else: res += sum(i)
  return res

