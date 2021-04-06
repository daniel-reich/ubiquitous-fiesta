
def count_number(lst):
  while any(type(i) == list for i in lst):
    flatten(lst)
  return sum([1 for i in lst if type(i) == int or type(i) == float])
  
​
def flatten(lst):
  for i in lst:
    if type(i) == list:
      lst += i
      del lst[lst.index(i)]
  return lst

