
def automorphic(n):
  
  numstring = str(n ** 2)
  print ("num %s" % n)
  print ("numString: %s" % numstring)
  lastChar = str(n)
  
  print (lastChar)
  
  return numstring.endswith(lastChar)

