
def sle(m):
  a,b,c,d,e,f=m[0]+m[1]
  if a/b==d/e:return False
  x=(f*b-c*e)/(d*b-a*e)
  return (round(x,0),round((c-a*x)/b,0))

