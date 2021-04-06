
### I = ligne
### J = colonne
​
def all_explode(grid):
  nb_fin = 0
  for i in grid:
    for j in i:
      if j == "+" or j == "x":
        nb_fin +=1
  
  grid = explosion(grid, 0,0)
  verif = 0
  for i in grid:
    for j in i:
      if j == 1:
        verif +=1
  print(grid, nb_fin, verif)
  if verif == nb_fin:
    return True
  return False
​
​
def explosion(grid, i, j):
  if grid[i][j] == "+":
    grid[i][j] = 1
    grid = explosion_plus(grid,i,j)
  elif grid[i][j] == "x":
    grid[i][j] = 1
    grid = explosion_croix(grid,i,j)
  return grid
[[1, 1, '0', 'x', 1, '+', '0'],
 ['0', 1, 1, 1, '0', '+', 'x']]
def explosion_plus(grid, i, j):
  lignes = len(grid)
  colonnes = len(grid[0])
  if i > 0:
    grid = explosion(grid, i-1, j)
  if j > 0:
    grid = explosion(grid, i, j-1)
  if i < lignes-1:
    grid = explosion(grid, i+1, j)
  if j < colonnes-1:
    grid = explosion(grid, i, j+1)
  return grid 
​
def explosion_croix(grid, i, j):
  lignes = len(grid)
  colonnes = len(grid[0])
  if i > 0 and j > 0:
    grid = explosion(grid, i-1, j-1)
  if i > 0 and j < colonnes-1:
    grid = explosion(grid, i-1, j+1)
  if i < lignes-1 and j > 0 :
    grid = explosion(grid, i+1, j-1)
  if i < lignes-1 and j < colonnes-1:
    grid = explosion(grid, i+1, j+1)
  return grid

