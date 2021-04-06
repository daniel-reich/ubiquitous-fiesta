
def harmonic(n):
  if(n == 0):
    return 0
  if(n == 1):
    return 1
  else:
    fact = 1
    #for i in range(1,(n+1)):
    # fact = fact*i
    f = 1 
    t = 1
    for i in range(2,(n+1)):
      t = i*t + f
      f = f*i
    r = float(0)
    r = float((t)/(f))
    r = round(r,3)
    return r

