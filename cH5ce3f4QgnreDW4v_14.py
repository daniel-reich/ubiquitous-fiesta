
def maximum_score(tile_hand):
  som = 0
  for i in tile_hand:
    som += i["score"]
  return som

