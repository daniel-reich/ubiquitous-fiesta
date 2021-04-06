
def min_swaps(s1, s2):
  a=0
  if len(s1)==len(s2) and s1.count("0")==s2.count("0") and s1.count("1")==s2.count("1"):
    for i in range(len(s1)):
      if s1[i]!=s2[i]:
        a+=1
    return a//2

