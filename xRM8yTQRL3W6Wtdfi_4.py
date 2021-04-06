
def quartic_equation(a, b, c):
  deta=b**2-4*a*c
  if deta<0:return 0
  elif deta==0:
    x=-b/(2*a)
    return 0 if x<0 else 1 if x==0 else 2
  else:
    x2=(-b-deta**0.5)/(2*a)
    if x2>0:
      return 4
    elif x2==0:
      return 3
    else:
      x1=(-b+deta**0.5)/(2*a)
      return 0 if x1<0 else 1 if x1==0 else 2

