
def cycle_length(lst, n):
  target = sorted(lst)
  swaps = 0
  while True:
    if lst[lst.index(n)] == lst[target.index(n)]:
      return swaps
    next_num = lst[target.index(n)]
    lst[lst.index(n)], lst[target.index(n)] = lst[target.index(n)], lst[lst.index(n)]
    swaps += 1
    n = next_num

