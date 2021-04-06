
def min_turns(current, target):
  temp1 = list(map(int,current))
  temp2 = list(map(int,target))
  result = 0
  for i in range(4):
    t = abs(temp1[i] - temp2[i]) 
    if t > 5:
      result += (10-t)
    else:
      result += t
  return result

