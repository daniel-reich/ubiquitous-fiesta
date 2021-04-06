
def boom_intensity(n):
  os = "o"*n
  if n < 2:
    return("boom")
  else:
    if ((n%2 == 0) and (n%5==0)):
      return("B" + os.upper() + "M!")
    elif (n%5 == 0):
      return("B" + os.upper() + "M")
    elif (n%2  == 0):
      return("B" + os + "m!")
    else:
      return("B" + os + "m")

