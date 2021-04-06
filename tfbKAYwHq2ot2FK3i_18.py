
def non_repeats(radix):
    tot = radix*(radix-1)
    for i in range(3,radix+1):
        tot+=(radix-1)*factorial(radix-1)//factorial(radix-i)
    return tot
  
def factorial(n):
    if n<=1: return 1
    return n*factorial(n-1)

