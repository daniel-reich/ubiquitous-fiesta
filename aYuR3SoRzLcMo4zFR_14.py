
def measure_the_depth(lst):
  count = 0
  for item in lst:
    if isinstance(item,list):
      count+= measure_the_depth(item)
​
  return count+1

