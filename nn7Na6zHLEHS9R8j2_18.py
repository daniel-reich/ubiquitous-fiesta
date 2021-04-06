
def deep_count(lst):
  return len(lst)+sum([deep_count(x) for x in lst if isinstance(x,list)])

