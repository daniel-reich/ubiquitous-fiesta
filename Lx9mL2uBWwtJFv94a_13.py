
def checker_board(n, el1, el2):
  if el1 == el2:
    return "invalid"
  d = {0:el1, 1:el2}
  lst = []
  for col in range(n):
      rl = []
      for row in range(n):
          rl.append(d[((col%2)+row)%2])
      lst.append(rl)
  return lst

