
def sle(m):
  try:a,b,c,d,e,f=sum(m,[]);x=(c*e-b*f)/(a*e-b*d);y=(f-d*x)/e;return(0,(x,y))[x!=y]
  except:return 0

