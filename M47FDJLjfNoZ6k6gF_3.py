
def cup_swapping(swaps):
  table = ['X','O','X']
  for swap in swaps:
    cup1 = 'ABC'.find(swap[0])
    cup2 = 'ABC'.find(swap[1])
    table[cup1],table[cup2] = table[cup2],table[cup1]
  return 'ABC'[table.index('O')]

