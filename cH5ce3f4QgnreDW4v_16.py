
def maximum_score(tile_hand):
  return sum(tile_hand[i].get("score") for i,row in enumerate(tile_hand))

