
def final(r, c, i):
  lst = [[0 for column in range(c)] for row in range(r)]
  for increment in i:
    if increment[-1] == "r":
      for each in range(len(lst[int(increment[:-1])])):
        lst[int(increment[:-1])][each] += 1
    else:
      for each in range(len(lst)):
        lst[each][int(increment[:-1])] += 1
  return lst

