
def can_put(txt, dim):
  txt = txt.split()
  row_count = dim[0]
  row_length = dim[1]
  
  n = 0
  
  while n < len(txt):
    if row_count < 1:
      return False
    row_count -= 1
    if len(txt[n]) > row_length:
      return False
    else:
      remaining_space = row_length - len(txt[n])
    if n+1 < len(txt) and remaining_space >= len(txt[n+1]) + 1:
      n += 2
    else:
      n += 1
      
  return True

