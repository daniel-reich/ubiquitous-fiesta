
def deep_count(lst):
  count = 0
  for i in lst:
    count = count + 1
    if isinstance(i,list):
      count = count + deep_count(i)
​
  return count

