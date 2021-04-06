
def swap(lst, ind):
  new_lst = lst.copy()
  new_lst[ind], new_lst[ind+1] = new_lst[ind+1], new_lst[ind]
  return new_lst
​
​
def number_of_swaps(lst):
  swaps = 0
  n = len(lst)
  while lst != sorted(lst):
    for ind in range(n-1):
      if lst[ind] > lst[ind+1]:
        lst = swap(lst, ind)
        swaps += 1
  return swaps

