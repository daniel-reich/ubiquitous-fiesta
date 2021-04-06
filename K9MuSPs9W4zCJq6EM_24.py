
def cycle_length(lst, n):
  count = 0
  sorted_lst = sorted(lst)
  test_index = lst.index(n)
  while test_index != sorted_lst.index(n):
    count += 1
    temp = lst[sorted_lst.index(n)]
    lst[sorted_lst.index(n)] = n
    n = temp
    lst[test_index] = n
  return count

