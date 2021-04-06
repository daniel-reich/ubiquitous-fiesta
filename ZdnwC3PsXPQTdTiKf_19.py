
def calculator(x,y,z):
  if z==0:
    return("Can't divide by 0!")
  else:
    if y=='+':
      return x+z
    elif y=='-':
      return x-z
    elif y=='*':
      return x*z
    else:
      return x/z

