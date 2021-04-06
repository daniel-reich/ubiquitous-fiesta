
def gen_deck():
  suits=['c','d','h','s']
  ans=[]
  for i in range(2,15):
    for j in suits:
      ans.append((i,j))
  return ans

