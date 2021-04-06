
def spin_around(lst):
  sum = 0
  for i in lst:
    if i == 'left':
      sum +=1
    elif i == 'right':
      sum +=-1
​
  return abs(sum) //4

