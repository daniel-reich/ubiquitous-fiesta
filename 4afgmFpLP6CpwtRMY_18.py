
def sudoku_validator(x):
  valid9 = (lambda lst9: all(dig in lst9 for dig in range(1,10)))
  
  sqr = (lambda top, left: [x[3*top + r][3*left + c] for r in range(3) for c in range(3)])
  row = (lambda top: [x[top][c] for c in range(9)])
  col = (lambda left: [x[r][left] for r in range(9)])
  
  sqrs_valid = all(valid9(sqr(top, left)) for top in range(3) for left in range (3))
  rows_valid = all(valid9(row(top)) for top in range(9))
  cols_valid = all(valid9(col(left)) for left in range(9))
​
  return sqrs_valid and rows_valid and cols_valid

