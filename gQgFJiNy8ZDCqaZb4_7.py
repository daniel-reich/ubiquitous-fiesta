
def overlap(s1, s2):
  res=""
  l=1
  for i in range(len(s1)):
      if s1[i]==s2[0]:
          l=len(s1)-i
          break   
  if s1[i:]==s2[:l]:
      res+=s1+s2[l:]
  elif s1==s2:
      res+=s1
  else:
      res+=s1+s2
  return res

