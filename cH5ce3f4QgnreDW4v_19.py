
def maximum_score(tile_hand):
  score=0
  for d in tile_hand:
    score = score + d["score"]  
  return score

