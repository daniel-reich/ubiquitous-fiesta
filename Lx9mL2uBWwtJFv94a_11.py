
def checker_board(n, el1, el2):
  if el1 == el2:
    return "invalid"
  w = [el1, el2]
  v0 = [w[i % 2 == 0] for i in range(n)]
  v1 = [w[i % 2 == 1] for i in range(n)]
  v, k = [v1, v0], 0
  r = []
  for i in range(n):
    r.append(v[k])
    k = 1 - k
  return r

