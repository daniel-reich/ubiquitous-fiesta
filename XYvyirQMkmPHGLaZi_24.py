
def boom_intensity(n):
  if n < 2:
    return "boom"
  a = "B" + n * "o" + "m"
  if n % 2 == 0 and n % 5 == 0:
    return a.upper() + "!"
  elif n % 2 == 0:
    return a + "!"
  elif n % 5 == 0:
    return a.upper()
  return a

