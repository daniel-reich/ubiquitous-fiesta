
def is_magic(square):
  size = len(square)
  magicNum =  (size**3 + size)/2
  # check rows:
  for row in square:
      if sum(row) != magicNum or len(row) != size:
          return False  
  # check columns:
  for col in range(size):
      column = [square[row][col] for row in range(size)]
      if sum(column) != magicNum:
          return False
          
  # check diagonals:
  if sum([square[i][i] for i in range(size)]) != magicNum:
      return False
  if sum([square[i][(size-1)-i] for i in range(size)]) != magicNum:
      return False
      
  # It must be magical then
  return True

