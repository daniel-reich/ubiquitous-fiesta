
def is_magic(square):
  size = len(square)
  magicNum =  (size**3 + size)/2
  for row in square:
      if sum(row) != magicNum or len(row) != size:
          return False  
  for col in range(size):
      column = [square[row][col] for row in range(size)]
      if sum(column) != magicNum:
          return False
  if sum([square[i][i] for i in range(size)]) != magicNum:
      return False
  if sum([square[i][(size-1)-i] for i in range(size)]) != magicNum:
      return False
  return True

