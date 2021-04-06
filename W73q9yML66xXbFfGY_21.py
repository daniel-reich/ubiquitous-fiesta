
def coloured_triangle(row):
  result = row
  if len(row) < 2:
    return row
  while len(result) > 1:
    temp_result = ""
    i = 0
    while i < len(result) - 1:
      merged_letters = return_new_color(result[i], result[i+1])
      temp_result += merged_letters
      i += 1
    result = temp_result
    print(result)
    
  return result
  
  
def return_new_color(c1, c2):
  if c1 == c2:
    return c1
  elif c1 == 'G':
    if c2 == 'R':
      return 'B'
    else:
      return 'R'
  elif c1 == 'R':
    if c2 == 'G':
      return 'B'
    else:
      return 'G'
  elif c1 == 'B':
    if c2 == 'G':
      return 'R'
    else:
      return 'G'

