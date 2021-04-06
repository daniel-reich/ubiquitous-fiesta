
def matmul(A,B):
    res=[[0,0],[0,0]]
    res[0][0]=A[0][0]*B[0][0]+A[0][1]*B[1][0]
    res[0][1]=A[0][0]*B[0][1]+A[0][1]*B[1][1]
    res[1][0]=A[1][0]*B[0][0]+A[1][1]*B[1][0]
    res[1][1]=A[1][0]*B[0][1]+A[1][1]*B[1][1]
    return res
def powmat(A,n):
    if n==1:
        return A
    else:
        return matmul(powmat(A,n//2), powmat(A,n//2)) 
def fibonacci(n):
  A=[[1,1],[1,0]]
  return powmat(A,n)[1][0]

