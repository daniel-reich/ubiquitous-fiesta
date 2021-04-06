
def checker_board(n, el1, el2):
  array_ell = []
  if(el1 == el2):
    return "invalid"
​
  for i in range(n):
    array_ell = array_ell + [[]]
    for j in range(n):
      if(i % 2 == 0):
        if j % 2 == 0:
          array_ell[i] += [el1]
        else:
          array_ell[i] += [el2]
      else:
        if j % 2 == 0:
          array_ell[i] += [el2]
        else:
          array_ell[i] += [el1]
​
  return array_ell

