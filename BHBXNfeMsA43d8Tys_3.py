
def pi(n):
  w=n+10
  b=10**w
  x1=b*4//5
  x2=b//-239
  he=x1+x2
  n*=2
  for i in range(3,n,2):
    x1//=-25
    x2//=-57121
    x=(x1+x2)//i
    he+=x
  pai=he*4
  pai//=10**10
  paistring=str(pai)
  result=paistring[0]+str('.')+paistring[1:len(paistring)]
  return  result

