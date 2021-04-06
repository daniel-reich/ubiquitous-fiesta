
def determinant(A):
  if len(A) == 1:
    return A[0][0]
  elif len(A) == 2:
    return A[0][0] * A[1][1] - A[1][0] * A[0][1]
  
  det = 0
  for column, value in enumerate(A[0]):
    sign = 1 if column % 2 == 0 else -1
    det += sign * value * determinant([
      [
        column_value
        for column_no, column_value in enumerate(row)
        if column_no != column
      ]
      for row_no, row in enumerate(A)
      if row_no != 0
    ])
  return det

