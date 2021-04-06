
def is_checkerboard(lst): 
  # Sum of indices is key. 
  # All numbers with even row+col must equal each other
  # All numbers with odd row+col must equal each other
  # evens cannot equal odds
  n = len(lst)
  for row in range(n):
    for col in range(n):
      if (row + col) % 2 == 0:   # indices sum to an even number
        if lst[row][col] != lst[0][0]:
          return False
      elif (row + col) % 2 == 1:   # indices sum to an odd number
        if lst[row][col] != lst[0][1]: 
          return False
  if lst[0][0] == lst[0][1]:
    return False
  return True

