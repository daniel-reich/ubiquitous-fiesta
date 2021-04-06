
def alternate_sort(l):
​
  lets = sorted( e for e in l if type(e) == str )
  nums = sorted( e for e in l if type(e) == int )
​
  return [ lets.pop(0) if i%2 else nums.pop(0) for i in range(0,len(lets)*2) ]

