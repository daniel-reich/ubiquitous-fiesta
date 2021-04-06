
def cup_swapping(swaps):
  cups = {'A': 0, 'B': 1, 'C': 0}
  
  for x, y in swaps:
    cups[x], cups[y] = cups[y], cups[x]
    
  return {v:k for k, v in cups.items()}[1]

