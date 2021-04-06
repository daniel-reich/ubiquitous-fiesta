
def boom_intensity(n):
  if(n < 2):
    return "boom"
  if(n % 5 == 0 and n % 2 == 0):
    return "B" + n * "O" + "M!" 
  if(n % 5 == 0):
    return "B" + n * "O" + "M"
  if(n % 2 == 0):
    return "B" + n * "o" + "m!"
  else:
    return "B" + n * "o" + "m"

