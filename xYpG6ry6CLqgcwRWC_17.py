
def sum_two_smallest_nums(lst):
  sorte = sorted(lst)
  smalL_total = 0
  for n in sorte:
    if n > 0:
      index = sorte.index(n)
      small_total = sorte[index] + sorte[index + 1]
      break
  return small_total

