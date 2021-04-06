
def cycle_length(lst, n):
  sorted_lst = sorted(lst)
  cycle_count = 0
  while True:
    a, b = lst.index(n), sorted_lst.index(n)
    if a == b:
      break
    lst[b], lst[a] = lst[a], lst[b]
    n = lst[a]
    cycle_count += 1
  return cycle_count

