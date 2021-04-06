
def is_apocalyptic(number):
  
  rawnum = str(2**number)
  print(rawnum)
  n = (rawnum.count("666"))
  print(n)
  d = {0:"Safe", 1:"Single", 2:"Double", 3:"Triple"}
  return(d[n])

