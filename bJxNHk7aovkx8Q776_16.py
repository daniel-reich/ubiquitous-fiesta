
def gold_distribution(gold):
  ans=[0,0]
  side=0
  while True:
    if len(gold)>2:
      if gold[0]<gold[-1]:
        ans[side]+=gold[-1]
        gold=gold[:-1]
      else:
        ans[side]+=gold[0]
        gold=gold[1:]   
      side=not side
    else:
      ans[side]+=max(gold)
      ans[not side]+=min(gold)
      return ans

