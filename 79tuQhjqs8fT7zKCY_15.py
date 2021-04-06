
def postfix(expr):
  a,b,c,d,e,f=[],[],[],[],[],[]
  
  if len(expr)==1:
    return(int(expr))
  
  expr=expr.split()
  
  if len(expr)==3:
    return (calc(expr))
  
  if len(expr)==5:
    return(calc([str(calc(expr))]+expr[3:]))  
  
  if len(expr)==7:
   a=calc(expr)
   b=[str(a)]+expr[3:]
   c=calc(b)
   if b[2]=="+" or b[2]=="-" or b[2]=="*" or b[2]=="/":
    d=[str(c)]+b[3:]
    return(calc(d))
   else:
    d=b[:1]+[str(c)]+b[4:]
    return(calc(d))
  
  if len(expr)>8:
   a=calc(expr)
   b=[str(a)]+expr[3:]
   c=calc(b)
   d=[str(c)]+b[3:]
   e=calc(d)
   f=d[:1]+[str(e)]+d[4:]
   return(calc(f))
 
def calc(a):
  if a[2]=="+" or a[2]=="-" or a[2]=="*" or a[2]=="/":
   return int(eval(a[0]+a[2]+a[1]))
  else:
   return int(eval(a[1]+a[3]+a[2]))

