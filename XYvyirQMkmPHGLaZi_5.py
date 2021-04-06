
def boom_intensity(n):
  if n < 2:
    return "boom"
    
  o_letters = "o" * n
  
  if n % 2 == 0 and n % 5 == 0:
    return "B" + o_letters.upper() + "M!"
  if n % 2 == 0:
    return "B" + o_letters + "m!"
  if n % 5 == 0:
    return "B" + o_letters.upper() + "M"
  else:
    return "B" + o_letters + "m"

