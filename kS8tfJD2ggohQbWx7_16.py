
def last_name(n):
  return n.split(" ")[1]
def last_name_lensort(names):
  names.sort(key = last_name)
  return sorted(names,key = lambda x: len(last_name(x)))

