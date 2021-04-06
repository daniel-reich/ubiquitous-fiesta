
def checker_board(n, el1, el2):
  if el1 == el2:
    return 'invalid'
  output = []
  lsteven = []
  while len(lsteven) < n:
    lsteven.append(el1)
    if len(lsteven) == n:
      break
    lsteven.append(el2)
  lstodd = []
  while len(lstodd) < n:
    lstodd.append(el2)
    if len(lstodd) == n:
      break
    lstodd.append(el1)
  for i in range(n):
    if i% 2 == 0:
      output.append(lsteven)
    else:
      output.append(lstodd)
  return output

