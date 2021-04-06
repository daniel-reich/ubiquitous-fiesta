
def num_grid(lst):
  mat = list(map(lambda r: (list(map(lambda c: 0 if c != "#" else "#", r))), lst))
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      if lst[i][j] == "#":
        update_mat(i, j, mat, lst)
  return list(map(lambda r: (list(map(lambda c: str(c) , r))), mat))
        
def update_mat(i, j, mat, lst):
  for di in range(-1, 2):
    for dj in range(-1, 2):
      ni = i + di
      nj = j + dj
      if ni >= 0 and ni < len(mat) and nj >= 0 and nj < len(mat[0]) and (ni != i or nj != j) and lst[ni][nj] != "#":
        mat[ni][nj] = mat[ni][nj] + 1

