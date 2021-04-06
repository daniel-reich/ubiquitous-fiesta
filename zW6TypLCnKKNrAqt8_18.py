
def is_smaller(tester, constant):
  return tester < constant
​
def left_side(lst):
  
  nl = []
  
  for n in range(len(lst)):
    tlist = lst[:n]
    con = lst[n]
    count = 0
    for item in tlist:
      if is_smaller(item, con) == True:
        count += 1
    nl.append(count)
  
  return nl
  
​
def right_side(lst):
    
  nl = []
  
  for n in range(len(lst)):
    tlist = lst[n+1:]
    con = lst[n]
    count = 0
    for item in tlist:
      if is_smaller(item, con) == True:
        count += 1
    nl.append(count)
  
  return nl

