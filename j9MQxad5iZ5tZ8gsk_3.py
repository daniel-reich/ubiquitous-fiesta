
def findVertex(eq):
  a,b,c=eq.replace(' ','',8).split('x')
  return -1*int(b)//(int(a)*2)   #  // is a workaround to the misstated problem

