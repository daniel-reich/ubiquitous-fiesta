
def completely_filled(lst):
  count_lt = 0
  for item in lst:
    len_ = len(item)
    if len_ < 3:
      return True
    count_lt += item.count('*')
  return count_lt == (len_-2)**2

