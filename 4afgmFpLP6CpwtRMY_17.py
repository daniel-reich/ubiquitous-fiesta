
def sudoku_validator(x):
​
  def checker(lst):
    return len(set(lst))==len(lst)
  
  #check the rows
  rowChk = []
  rowChk = [checker(n) for n in x]
  
  #check the columns
  colChk = []
  for c in range(9):
    col = [row[c] for row in x]
    colChk.append(checker(col))
  
  #check the 3X3 boxes
  boxChk = []
  for j in range(0,9,3):
    for i in range(0,9,3):
      box = [x[r][c] for c in range(0+j,3+j) for r in range(0+i,3+i)]
      boxChk.append(checker(box))
  
  
  return all(rowChk)==True and all(colChk)==True and all(boxChk)==True

