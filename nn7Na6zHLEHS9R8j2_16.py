
def deep_count(lst):
  return sum([1 if type(i)!=list else 1+deep_count(i) for i in lst])

