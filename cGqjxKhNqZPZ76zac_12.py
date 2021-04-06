
def fire(m, c):
  x = ['A','B','C','D','E'].index(c[0])
  y = int(c[1])-1
  return "splash" if m[x][y] == '.' else 'BOOM'

