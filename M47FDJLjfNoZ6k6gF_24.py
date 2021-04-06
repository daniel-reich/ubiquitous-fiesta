
def cup_swapping(swaps):
  current = 'B'
  for i in swaps:
    if current in i:
      if current == i[0]:
        current = i[1]
      else:
        current = i[0]
  return current

