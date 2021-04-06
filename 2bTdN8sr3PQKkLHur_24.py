
def divisible_by_b(a, b):
    rem = (a + b) % b;  
    if (rem == 0):  
      return a
    else: 
      return (a + b - rem)

