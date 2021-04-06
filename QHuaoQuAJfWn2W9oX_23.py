
def check_board(col, row):
  col = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,"f": 5,"g": 6,"h": 7}[col]
  row = row-1
  result = []
  for i in range(8):
    temp = []
    for j in range(8):
      if i == row and j == col: temp.append(0)
      elif i == row or j == col: temp.append(1)
      elif abs(col - j) == abs(row - i): temp.append(1)
      else: temp.append(0)
    result = [temp] + result
  return result

