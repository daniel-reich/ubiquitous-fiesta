
def dice_game(lst):
  tmp = [sum(i) for i in lst if i[0]!=i[1]]
  return sum(tmp) if len(tmp) == 3 else 0

