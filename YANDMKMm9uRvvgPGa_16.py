
def same(a1, a2):
  if len(set(a1)) == len(set(a2)):
    return True
  else:
    return False
  
  
​
same([1, 3, 4, 4, 4], [2, 5, 7])

