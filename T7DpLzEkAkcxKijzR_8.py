
def cars_needed(n):
  x=n/5
  x_int=x.is_integer()
  if(x_int == True):
    return x
  else:
    return (int(x)+1)

