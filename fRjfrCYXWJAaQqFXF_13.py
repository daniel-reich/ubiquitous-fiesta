
def primorial(n):
  
  def is_prime(num):
    for i in range(2, num):
      if num%i == 0:
        return False
    return True
​
  def next_prime():
    i = 2
    while True:
      if is_prime(i):
        yield i
      i += 1
      
  primorial = 1
  p = next_prime()
​
  for i in range(n):
    primorial *= next(p)
​
  return primorial

