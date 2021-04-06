
def poker_hand_ranking(hand):
  print("__________________________")
  rank={"A":14, "K":13, "Q":12, "J":11}
  hand=[[rank[i[:-1]],i[-1]] if rank.get(i[:-1]) is not None else[int(i[:-1]),i[-1]]  for i in hand]
  straight=max(h for h,r in hand)-min(h for h,r in hand)==4
  royal=max(h for h,r in hand)==14
  
  pairs={}
  ranks={}
  for i,j in hand:
    if pairs.get(i)==None:
      pairs[i]=1
    else:
      pairs[i]+=1
    if ranks.get(i)==None:
      ranks[j]=1
    else:
      ranks[j]+=1
​
  flush=len(ranks)==1
  if len(pairs)==2:
    if max(pairs.values())==4:
      return "Four of a Kind"
    else:
      return "Full House"
  elif len(pairs)==3:
    if max(pairs.values())==3:
      return "Three of a Kind"
    else:
      return "Two Pair"
  elif len(pairs)==4:
      return "Pair"
  elif flush and royal and straight:
    return "Royal Flush"
  elif flush and straight:
    return "Straight Flush"
  elif flush:
    return "Flush"
  elif straight:
    return "Straight"
  else:
    return "High Card"

