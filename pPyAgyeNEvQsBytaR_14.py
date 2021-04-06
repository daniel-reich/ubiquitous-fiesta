
def factorial(n):
  #base case
  if(n <= 1):
    return 1
    
  #inductive case
  else:
    return n * factorial(n-1)

