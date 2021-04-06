
def mubashir_function(a, b):
  if a < 10 and b < 10:
    return a*b
  elif a%10==0 and b%10==0:
    return int(str(a*b)[0])
  elif a%10 and b%10:
    return int(str(min([a,b]))[::-1])

