
def make_transpose(m):
  rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
  return rez

