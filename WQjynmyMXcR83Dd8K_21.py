
def number_of_swaps(lst):
  x = sorted(lst)
  cnt = 0
  while lst != x:
    for i in range(len(lst) - 1):
      if lst[i] > lst[i + 1]:
        lst[i],lst[i + 1] = lst[i + 1], lst[i]
        cnt += 1
  return cnt

