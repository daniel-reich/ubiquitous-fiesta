
def bemirp(n):
  if not is_prime(n): return 'C'
  if not is_prime(flip(n)) or flip(n) == n: return 'P'
  if not is_prime(up_down(n)): return 'E'
  return 'B'
  
def flip(n):
  return int(str(n)[::-1])
​
def up_down(n):
  dic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
  return int(''.join(dic.get(d, 'False') for d in str(n)))
​
def is_prime(n):
  return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

