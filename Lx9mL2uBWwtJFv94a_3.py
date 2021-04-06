
def checker_board(n, el1, el2):
  if el1 == el2: return 'invalid'
  liAppend = []
  for a in range(0, n + 1, 1):
    if a % 2 == 0: liAppend.append(el1)
    else: liAppend.append(el2)
  li1 = liAppend[:n]
  li2 = liAppend[1:]
  res = []
  for a in range(0, n, 1):
    if a % 2 == 0: res.append(li1)
    else: res.append(li2)
  return res

