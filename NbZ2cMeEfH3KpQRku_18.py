
from functools import reduce
def happy(l):
  res = (1 if l[0] == l[1] else 0) + (1 if l[-1] == l[-2] else 0)
  print(res)
  #print([(i,x) for i,x in filter(lambda x: x[0] != 0 and x[0] != len(l)-1,enumerate(l))])
  res += reduce(lambda a,b:a + 1 if l[b[0]] == l[b[0]-1] or l[b[0]] == l[b[0]+1] else 0 ,filter(lambda x: x[0] != 0 and x[0] != len(l)-1,enumerate(l)),0)
  #print(res)
  return res  
    
def portion_happy(numbers):
  hap = happy(numbers)
  #print(hap,len(numbers)-hap)
  return happy(numbers)/(len(numbers))
print(percentage_happy([1, 0, 0, 1, 1]))

