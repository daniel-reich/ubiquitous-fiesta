
def maximum_score(tile_hand):
  ans = 0
  for i in tile_hand:
    ans+=i["score"]
  return ans

