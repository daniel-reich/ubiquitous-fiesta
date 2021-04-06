
def dice_roll(n, outcome):
  if n == 1:
    return 1 if 1<=outcome<=6 else 0
  return sum([dice_roll(n-1, outcome-N) for N in [1,2,3,4,5,6] if N<outcome])

