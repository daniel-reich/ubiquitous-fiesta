
def is_shifted(lst1, lst2):
  return all([lst1[0]-lst2[0]==lst1[i]-lst2[i] for i in range(len(lst2))])
​
def is_multiplied(lst1, lst2):
  if all(map(lambda x: not x,lst1)) or all(map(lambda x: not x,lst2)): return True
  else: return all([lst1[0]*lst2[i]==lst2[0]*lst1[i] for i in range(len(lst2))])

