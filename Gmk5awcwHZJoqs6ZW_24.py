
def largest_island(lst):
  def search(a,b):
    for i in range (len(lst)):
      for j in range (len(lst[0])):
        if lst[i][j]==a:
          lst[i][j] = b
          return [i,j]
    return False
  def check_adjacent(coordinates):
    x,y = coordinates[0],coordinates[1]
    for d in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
      if -1 < x+d[0] < len(lst) and -1 < y+d[1] < len(lst[0]) and lst[x+d[0]][y+d[1]]==1:
        lst[x+d[0]][y+d[1]] = n
  n = 2
  while search(1,1)!=False:
    check_adjacent(search(1,n+1))
    while search(n,n)!=False:
      check_adjacent(search(n,n+1))
    n += 2
  islands = [i for j in lst for i in j if i!=0]
  return max(islands.count(i) for i in islands)

