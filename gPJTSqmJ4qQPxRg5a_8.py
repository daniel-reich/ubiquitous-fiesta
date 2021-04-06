
import math
def func(num):
  x = num
  count = 1
  list = []
  sum = 0
  while x>10:
    list.append(x%10)
    count+=1
    x=math.floor(x/10)
  list.append(x%10)
  for i in range(len(list)):
    sum+=(list[i]-count)
  return sum

