
def fire(matrix, coordinates):
​
  row, column = [i for i in coordinates]
  row = ord(row) - 65
  column = int(column) - 1
​
  return "BOOM" if matrix[row][column] == "*" else "splash"

