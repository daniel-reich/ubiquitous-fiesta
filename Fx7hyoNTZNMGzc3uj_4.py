
def number_len_sort(lst):
  n = []
  count = 1
  
  while len(n) != len(lst):
    for i in lst:
      if len(str(i)) == count:
        n.append(i)
    count += 1
  
  return n

