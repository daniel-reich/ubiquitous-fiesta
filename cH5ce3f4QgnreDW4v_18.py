
def maximum_score(tile_hand):
  res = 0
  for di in tile_hand:
    res += di["score"]
  return res

