
def spiral_transposition(lst):
  fl = []
  m = len(lst)
  n = len(lst[0])
  k, l = 0, 0
​
  while (k < m) and (l < n):
    for i in range(l, n):
      fl.append(lst[k][i])
    k = k+1
    
    for i in range(k, m):
      fl.append(lst[i][n-1])
    n = n-1
    
    for i in range(n, l, -1):
      fl.append(lst[m-1][i-1])
    m = m-1
    
    for i in range(m-1, k-1, -1):
      fl.append(lst[i][l])
    l = l+1
    
  return fl

