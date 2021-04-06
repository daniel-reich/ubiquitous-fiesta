
def collatz(num):
  #base case
  if(num == 1):
    return 0
    
  #if n is even -> n / 2  
  if (num % 2 == 0):
    return 1 + collatz(num/2) 
  
  #if n is odd -> n * 3 + 1
  else:
    return 1 + collatz(num * 3 + 1)

