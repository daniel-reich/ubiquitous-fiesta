
def multiplier(lst, count):
  if len(lst)==1:
    return count;
  else:
    count+=1
    total=1
    for i in lst:
      total=total*i
    total = [int(i) for i in str(total)]
    return multiplier(total, count)
  
​
def bugger(num):
  x = [int(i) for i in str(num)]
  return multiplier(x, 0)

