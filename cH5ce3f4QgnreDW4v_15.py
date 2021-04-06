
def maximum_score(tile_hand):
  return sum(tile_hand[i]['score'] for i in range(len(tile_hand)))

