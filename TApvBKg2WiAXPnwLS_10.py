
def nth_smallest(lst, n):
  new_lst = sorted(lst)
  for i in range(len(lst)):
    if i+1 == n:
      return new_lst[i]

