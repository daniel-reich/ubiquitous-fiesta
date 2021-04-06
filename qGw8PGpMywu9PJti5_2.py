
def hanoi(n):
  
  def han(i,j,n):
    if n==0:
      return []
    k = 6-i-j
    return han(i,k,n-1) + [(i,j)] + han(k,j,n-1)
  
  return han(1,3,n)

