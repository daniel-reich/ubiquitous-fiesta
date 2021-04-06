
def ordinal(n):
  s='tsnrhtdd'
  return '{}'.format(s[(n//10%10!=1)*(n%10<4)*(n%10)::4])
def is_polygonal(n):
  if n!=1 and n<1000:
    A=[]
    for i in range(1,n):
      for j in range(3, n):
        if (i-1)*i*j==2*(n-1):
          A.append((i-1,j))
    A=sorted(A, key=lambda x: x[1])
    B=[ordinal(x[0]) for x in A]
    C=['{0}{1} {2}-gonal number'.format(A[i][0], B[i], A[i][1]) for i in range(len(A))]
    return C if A else False
  elif n==1:
    return "0th of all"
  else:
    quit()

