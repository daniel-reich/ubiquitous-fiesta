
def valid(st1,st2):
  big,small = (st1,st2)  if len(st1) > len(st2)  else  (st2,st1)
  print(big,small)
  s2b_map = [None for i in range(len(big))]
  
  for i,s in enumerate(small):
    for j,b in enumerate(big):
      if j<i:
        continue
      if b == s and s2b_map[j] == None:
        s2b_map[j] = i
        break
​
  print(s2b_map)  
​
  diffs = 0
  last = None
  for m in s2b_map:
    if m == None:
      diffs += 1
    elif last != None and m<last:
        diffs += 1
    last = m
  
​
  print(s2b_map)
  print(diffs)
  return diffs == 1
​
    
def isWordChain(words):
  first = words[0]
  for word in words[1:]:
    if not valid(first,word):
      return False
    first = word
  return True

