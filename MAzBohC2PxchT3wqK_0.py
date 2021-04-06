
def shadow_sentence(a, b):
  A=a.split()
  B=b.split()
  return  len(A)==len(B) and all(len(A[i])==len(B[i]) and set(A[i])&set(B[i])==set() for i in range(len(A)))

