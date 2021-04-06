
def get_diagonals(pos):
  diag = []
  x = pos[0]
  y = pos[1]
  while x < 'h' and y < '8':
    x = chr(ord(x) + 1)
    y = str(int(y) + 1)
    diag.append(x + y)
  x = pos[0]
  y = pos[1]
  while x > 'a' and y > '1':
    x = chr(ord(x) - 1)
    y = str(int(y) - 1)
    diag.append(x + y)
  x = pos[0]
  y = pos[1]
  while x < 'h' and y > '1':
    x = chr(ord(x) + 1)
    y = str(int(y) - 1)
    diag.append(x + y)
  x = pos[0]
  y = pos[1]
  while x > 'a' and y < '8':
    x = chr(ord(x) - 1)
    y = str(int(y) + 1)
    diag.append(x + y)
  return diag
  
def bishop(start, end, n):
  if start == end:
    return True
  if n == 0:
    return False
  for pos in get_diagonals(start):
    if bishop(pos, end, n - 1):
      return True
  return False

