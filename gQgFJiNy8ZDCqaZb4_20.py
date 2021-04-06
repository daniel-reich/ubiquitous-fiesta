
def overlap(s1, s2):
  if s1 == s2:
    return s1
​
  current = 1
  cond = True
  j = 0
  for i in range(len(s1), 0, -1):
    if s1[i-1:] == s2[:j+1]:
      current = i
      cond = False
    j += 1   
​
  if cond == True:
    return s1 + s2
  return s1[:current-1] + s2

