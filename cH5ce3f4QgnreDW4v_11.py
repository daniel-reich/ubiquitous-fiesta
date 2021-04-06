
def maximum_score(tile_hand):
  a = 0
  for i in range(len(tile_hand)):
    a += tile_hand[i]['score']
  return a

