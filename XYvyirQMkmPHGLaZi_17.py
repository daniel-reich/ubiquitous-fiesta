
def boom_intensity(n):
  if n < 2:
    return "boom"
  elif n%2 == 0 and n%5 == 0:
    return "B"+ "O"*n +"M"+"!"
  elif n%2 == 0:
    return "B"+ "o"*n +"m" +"!"
  elif n%5 == 0:
    return "B"+ "O"*n +"M"
  else:
    return "B"+ "o"*n +"m"

