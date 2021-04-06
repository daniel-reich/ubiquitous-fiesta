
def coloured_triangle(row):
  ans = ''
  for a, b in zip(row, row[1:]):
    if(a == b): 
      ans += a
    elif(a + b == 'GB' or a + b == 'BG'):
      ans += 'R'
    elif(a + b == 'RG' or a + b == 'GR'):
      ans += 'B'
    else:
      ans += 'G'
  return row if len(row) == 1 else coloured_triangle(ans)

