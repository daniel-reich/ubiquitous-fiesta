
def is_shifted(lst1, lst2):
  return lst1[0]-lst2[0] == lst1[1]-lst2[1] == lst1[2]-lst2[2]
​
def is_multiplied(lst1, lst2):
  return lst1[0]*lst2[1] == lst1[1]*lst2[0] and lst1[1]*lst2[2] == lst1[2]*lst2[1]

