
def sudoku_validator(x):
  chk = list(range(1,10))
  hoz = all(sorted(row)==chk for row in x)
  ver = all(sorted(col)==chk for col in list(map(list,zip(*x))))
  arr = []
  for i in range(0,len(x),3):
    for j in range(0,len(x),3):
      tmp = []
      for a in range(3):
        for b in range(3):
          tmp.append(x[i+a][j+b])
      arr.append(tmp)
  squ = all(sorted(row) == chk for row in arr)
  return hoz and ver and squ

