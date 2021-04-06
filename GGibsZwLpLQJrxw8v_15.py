
def get_lucky_number(size, nth):
  lst = list(range(1, size + 1, 2))
  for i in range(1, size + 1):
    if len(lst) <= i: break
    for j in range(lst[i] - 1, size, lst[i]):
      if j >= len(lst): break
      lst[j] = 0
    lst = [x for x in lst if x]
  return lst[nth - 1]

