
def dice_game(lst):
  final = []
  for x in lst:
    if len([x for x in lst if x[0] == x[1]]) == 0:
      final += x
    else:
      return 0
  return sum(final)

