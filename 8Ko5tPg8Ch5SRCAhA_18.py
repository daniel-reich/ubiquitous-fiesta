
def fibonacci(num):
  Phi = (1 + 5**0.5) / 2
  return (Phi**(num+1) - (-Phi)**(-num-1)) // 5**0.5

