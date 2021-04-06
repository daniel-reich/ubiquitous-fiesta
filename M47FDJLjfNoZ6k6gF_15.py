
def cup_swapping(swaps):
  ans = "B"
  for i in swaps:
    if ans in i: ans = i[i.index(ans)-1]
  return ans

