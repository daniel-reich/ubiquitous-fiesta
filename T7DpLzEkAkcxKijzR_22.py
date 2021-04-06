
def cars_needed(n):
  
  if(n%5==0):
    return n/5
  elif(n==0):
    return n
  else:
    return (n//5)+1

