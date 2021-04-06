
def filter_list(l):
  integers = []
  for x in l:
    if isinstance(x, int): 
      integers.append(x)
  return integers

