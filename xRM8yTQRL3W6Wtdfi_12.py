
def quartic_equation(a, b, c):
  t1=(-b+(b*b-4*a*c)**.5)/(2*a)
  t2=(-b-(b*b-4*a*c)**.5)/(2*a)
  if t1>0 and t2>0:
    return 4
  elif (t1>0 and t2<0) or (t1<0 and t2>0):
    return 2
  elif (t1==0 and t2>0) or (t1>0 and t2==0):
    return 3
  elif t1==t2 and t1>0:
    return 1
  elif t1==t2==0:
    return 1
  elif (t1==0 and t2<0) or (t1<0 and t2==0):
    return 1
  else:
    return 0

