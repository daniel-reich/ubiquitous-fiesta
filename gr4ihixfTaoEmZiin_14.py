
def add_indexes(lst):
  ret = []
  count = 0
  for item in lst:
    ret.append(item + count)
    count += 1
  return ret

