
def cup_swapping(swaps):
  pos = 'B'
  for move in swaps:
    pos = move.replace(pos, '') if pos in move else pos
  return pos

