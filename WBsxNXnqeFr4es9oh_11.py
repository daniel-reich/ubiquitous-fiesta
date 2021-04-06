
from math import ceil
def clockwise_cipher(message):
  n = ceil(len(message)**0.5)
  getcoords = lambda n: [[],[[0,0]]][n] if n<2 else \
    sum(([[0,i],[i,n-1],[n-1,n-1-i],[n-1-i,0]] for i in range(n-1)),[])+[
    [j+1 for j in i] for i in getcoords(n-2)]
  coords,grid = getcoords(n),[[" "]*n for _ in range(n)]
  for x in range(len(message)):
    a,b = coords[x]; grid[a][b] = message[x]
  return ''.join(sum(grid,[]))

