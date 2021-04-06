
def checker_board(n, el1, el2):
  if el1 == el2:
    return "invalid"
    
  if n % 2 == 0:
    row1 = [el1, el2] * int(n / 2)
    row2 = [el2, el1] * int(n / 2)
  else:
    row1 = [el1] + ([el2, el1] * int((n - 1) / 2))
    row2 = [el2] + ([el1, el2] * int((n - 1) / 2))
    
  result = []
  for i in range(n):
    if i % 2 == 0:
      result.append(row1)
    else:
      result.append(row2)
  return result

