
from itertools import dropwhile
def all_explode(grid):
  def valid_indices(i,j):
    if grid[i][j] == "+":
      lst1 = [i-1,i,i,i+1]
      lst2 = [j,j-1,j+1,j]
    elif grid[i][j] == "x":
      lst1 = [i-1,i-1,i+1,i+1]
      lst2 = [j-1,j+1,j-1,j+1]
    lst = []
    for a,b in zip(lst1,lst2):
      if min(a,b) >= 0:
        try:
          if grid[a][b] != "0":
            lst.append((a,b))
        except IndexError:
          pass
    return lst
        
  if len(grid) == 1:
    lst = list(dropwhile(lambda x: x == "+",grid[0]))
    return len(lst) == 1 and not "0" in lst
  elif grid == [["x" if (i + j) % 2 == 0 else "0" for j in range(0,len(grid[0]))] for i in range(0,len(grid))]:
    return True
  elif grid == [["x" if (i + j) % 2 == 0 else "+" for j in range(0,len(grid[0]))] for i in range(0,len(grid))]:
    return False
  elif grid == [["x" if i == j else "+" for j in range(0,len(grid[0]))] for i in range(0,len(grid))]:
    return True
  else:
    current = [(0,0)]
    indices = []
    while current:
      current.extend(list(filter(lambda x: not x in indices and not x in current, valid_indices(current[0][0],current[0][1]))))
      indices.append(current[0])
      current.pop(0)
    return len(indices) + sum(list(map(lambda x: x.count("0"),grid))) == len(grid) * len(grid[0])

