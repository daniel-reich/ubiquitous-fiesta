
def can_capture(queens):
  print(queens)
  map = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
  print(map.get(queens[0][0]))
  print(map.get(queens[1][0]))
  diff_column = abs(map.get(queens[0][0]) -  map.get(queens[1][0]))
  diff_row = abs(int(queens[0][1]) - int(queens[1][1]))
  
  if queens[0][0] == queens[1][0]:
    # same colums
    return True
  elif queens[0][1] == queens[1][1]:
    # same row
    return True
  elif diff_column == diff_row:
    print(diff_column)
    print(diff_row)
    return True
  else:
    return False

