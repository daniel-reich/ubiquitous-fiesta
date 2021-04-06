
def numbers_need_friends_too(n):
  n = str(n)
  a,z = n[0]*[3,1][n[1]==n[0]],n[-1]*[3,1][n[-2]==n[-1]]
  lst = [v*[3,1][v in [n[i-1],n[i+1]]] for i,v in enumerate(n[1:-1],1)]
  return int(a+''.join(lst)+z)

