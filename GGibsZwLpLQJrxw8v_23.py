
def get_lucky_number(size, nth):
  lst = [x for x in range(1, size+1)]
  used = [1]
  while True:
    for i in lst:
      if not i in used:
        used.append(i)
        if used[-1] > len(lst):
          return lst[nth-1]
        break
    for i in range(used[-1]-1, len(lst), used[-1]):
      lst[i] = "x"
    while "x" in lst:
      del lst[lst.index("x")]

