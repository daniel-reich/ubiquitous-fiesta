
def babbage(n):
  for i in range(1,n+1):
    if n == 269696 : 
      return "Babbage was {}!".format("correct" if str(i**2).endswith(str(n)) else "incorrect" )
    else:
      if str(i**2).endswith(str(n)):
        return i

