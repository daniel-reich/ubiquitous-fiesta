
def n_differences(lst):
  total = []
  while len(total) != 1:
    for x in range(len(lst)):
      try:
        total.append(lst[x+1]- lst[x])
      except:
        lst = total
        print(lst)
  return total

