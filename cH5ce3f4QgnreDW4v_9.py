
def maximum_score(tile_hand):
  rv=0
  for x in tile_hand:
    rv+=x["score"]
  return rv

