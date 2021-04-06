
def probability(lst, n):
  new_lst = []
  for num in lst:
    if num >= n:
      new_lst.append(num)
  
  return round((len(new_lst) / len(lst)) * 100, 1)

