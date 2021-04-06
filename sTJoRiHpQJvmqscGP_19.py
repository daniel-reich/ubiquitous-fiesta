
def daily_streak(lst):
  ans=0
  ans2=0
  for i in lst:
    if i: 
      ans2+=1
      if ans2>ans: ans=ans2
    else: ans2=0
  return ans

