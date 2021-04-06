
def make_grlex(lst):
  sort = sorted(lst, key= str.lower)
  sum_len = 0
  for word in lst:
    sum_len += len(word) 
  length = sum_len / len(lst)
  if length != len(sort[0]):
    return sorted(sort, key=len)
  else:
    return sort

