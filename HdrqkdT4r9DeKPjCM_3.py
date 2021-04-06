
def is_polygonal(n):
  th=lambda n:"%d%s " % (n,'tsnrhtdd'[(n//10%10!=1)*(n%10<4)*n%10::4])
  a,s=[],lambda n: n*(n+1)//2
  if n<4: return ["0th of all",False,False][n-1]
  for i in range(1,n//2):
    if (n-1)%s(i)==0:
      k=(n-1)//s(i)
      if k>2: a+=[th(i)+str(k)+'-gonal number']
  return a[::-1]

