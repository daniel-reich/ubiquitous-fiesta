
def is_magic(square):
  d1 = None
  d2 = None
  numbers = None
  try:
    d1 = sum(list(map(lambda x: square[x][x],range(0,len(square)))))
    d2 = sum(list(map(lambda x: square[len(square)-1-x][x],range(0,len(square)))))
  except IndexError:
    pass
  try:
    numbers = [square[n // len(square)][n % len(square)] for n in range(0,pow(len(square),2))]
  except IndexError:
    pass
  def cols(j):
    return sum([square[i][j] for i in range(0,len(square))])
    
  if not square:
    return True
  elif min(list(map(lambda x: len(x),square))) != max(list(map(lambda x: len(x),square))):
    return False
  elif len(square) != len(square[0]):
    return False
  elif sorted(numbers) != list(range(1,pow(len(square),2)+1)):
    return False
  elif d1 != d2:
    return False
  elif any(list(map(lambda x: sum(x) != d1,square))):
    return False
  else:
    return all(list(map(lambda x: cols(x) == d1,range(0,len(square)))))

