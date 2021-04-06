
def is_shifted(lst1, lst2):
  return len(set([lst2[i]-lst1[i] for i in range(len(lst1))]))==1
​
def is_multiplied(lst1, lst2):
  return len(set([lst2[i]/lst1[i] for i in range(len(lst1))]))==1

