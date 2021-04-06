
def make_row_odd(n, el1, el2):
  Colcounter = 0
  line = []
  while Colcounter < n:
    if Colcounter % 2 == 0:
      line.append(el1)
    else:
      line.append(el2)
    Colcounter += 1
  return line
​
def make_row_even(n, el1, el2):
  Colcounter = 0
  line = []
  while Colcounter < n:
    if Colcounter % 2 == 0:
      line.append(el2)
    else:
      line.append(el1)
    Colcounter += 1
  return line
  
def build_board(n, el1, el2):
  Rowcounter = 0
  result = []
  while Rowcounter < n:
    if Rowcounter % 2 == 0:
      result.append(make_row_odd(n, el1, el2))
    else:
      result.append(make_row_even(n, el1, el2))
    Rowcounter += 1
  print(result)
  return result
​
def checker_board(n, el1, el2):
  if el1 == el2:
    return "invalid"
  else:
    return build_board(n, el1, el2)

