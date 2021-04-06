
def cup_swapping(swaps):
  pos='B'
  for i in swaps:
    if pos in i:
      pos=''.join([j for j in i if j!=pos])
  return pos

