
def is_shifted(lst1, lst2):
  return all(lst1[i]-lst2[i] == lst1[i-1]-lst2[i-1] for i in range(1,len(lst1)))
​
def is_multiplied(lst1, lst2):
  return all(lst2[i]/lst1[i] == lst2[i-1]/lst1[i-1] for i in range(1,len(lst1)))

