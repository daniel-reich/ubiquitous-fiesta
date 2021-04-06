
def checker_board(n, el1, el2):
  res = []
  if el1 != el2:
    for i in range(n):
      l= []
      if i % 2 == 0:
        for j in range(n):
          if j % 2 == 0:
            l.append(el1)
          else:
            l.append(el2)
      else:
        for j in range(n):
          if j % 2 == 0:
            l.append(el2)
          else:
            l.append(el1)
      res.append(l)
    return res
  else:
    return 'invalid'

