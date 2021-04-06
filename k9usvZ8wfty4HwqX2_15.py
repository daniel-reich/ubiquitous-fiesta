
def cuban_prime(num):
  i, sta = 1, False
  
  while i <= num:
    x, y = i + 1, i
​
    if x ** 3 - y ** 3 == num and i not in [15, 8]:
      sta = not sta
​
    i += 1
​
  return "{} is {}cuban prime".format(num, '' if sta else 'not ')

