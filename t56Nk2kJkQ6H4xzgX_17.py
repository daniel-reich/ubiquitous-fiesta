
def swap_xy(txt):
  import re
  ans = [coordinate.strip() for coordinate in re.split('[\(\),*]', txt) \
  if coordinate.strip()]
  odd = [i for no, i in enumerate(ans) if no%2 == 1]
  even = [i for no, i in enumerate(ans) if no%2 == 0]
  ans = ', '.join(['('+i+', '+j+')' for i, j in zip(odd,even)])
  return ans

