
def min_swaps(s1, s2):
  cnt=0
  for i in range(0,len(s1)):
    if s1[i]!=s2[i]:
      cnt+=1
  return cnt//2

