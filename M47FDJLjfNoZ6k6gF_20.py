
def cup_swapping(swaps):
  cup = 'B'
  for sw in swaps:
    if cup in sw:
      cup = sw[1] if cup == sw[0] else sw[0]
  return cup

