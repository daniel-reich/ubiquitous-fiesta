
def maximum_score(tile_hand):
  total = 0
  for x in tile_hand:
   x = dict(x)
   x = x.get("score")
   total += x
  return total

