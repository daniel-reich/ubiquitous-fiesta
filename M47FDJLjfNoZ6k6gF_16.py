
def cup_swapping(swaps, p='B'):
  for i in swaps:
    if p in i:
      p = i.replace(p,'')
  return p

