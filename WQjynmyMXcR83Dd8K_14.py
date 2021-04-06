
def number_of_swaps(lst):
  i = 1
  k = 0
  a = 0
  while i < len(lst):
    c = 1
    while c < len(lst):
      if lst[c] < lst[c-1]:
        a = lst[c-1]
        lst[c-1] = lst[c]
        lst[c] = a
        k += 1
      c += 1
    i += 1
  return k

