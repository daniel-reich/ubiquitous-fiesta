
def shortest_path(lst):
  n,m = len(lst),len(lst[0])
  data = sorted([(lst[i][j],i,j) for i in range(n) for j in range(m) if \
    lst[i][j]!='0'])
  return sum(abs(p[1]-data[idx][1]) + abs(p[2]-data[idx][2])
          for idx,p in enumerate(data[1:]))

