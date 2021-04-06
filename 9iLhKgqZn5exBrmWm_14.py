
from functools import reduce
​
def ascending(txt):
  counter = 1
​
  while(counter <= (len(txt)//2)):
    lst = [int(item) for item in create_list(txt, counter)]
    results = []
​
    for i in range(0, len(lst)):
      if(i+2 <= len(lst)):
        results.append(reduce(lambda a, b: True if ((a+1) == b) else False, lst[i:i+2]))
​
    if(all(results)):
      return True
    else:
      counter += 1
  return False
def create_list(lst, n):
  result = []
​
  for i in range(0, len(lst), n):
    result.append(lst[i:i+n])
​
  return result

