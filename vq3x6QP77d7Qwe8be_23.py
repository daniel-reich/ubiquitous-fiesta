
def odd_square_patch(lst):
  def get_square(y,x,n):
    if y + n > len(lst) or x + n > len(lst[0]):
      return False
    for r in range (y,y+n):
      for c in range (x,x+n):
        if lst[r][c] % 2==0:
          return False
    return True
  max_square = 0
  for row in range (len(lst)):
    for column in range (len(lst[0])):
      size = 1
      while True:
        if not get_square(row,column,size):
          if size-1 > max_square:
            max_square = size-1
          break
        size += 1
  return max_square

