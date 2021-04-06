
def bemirp(n):
  if prime(n):
    if n!= int(str(n)[::-1]) and prime(int(str(n)[::-1])):
      if prime(int(str(n).replace('6','#').replace('9','6').replace('#','9'))):
        return 'B'
      return 'E'
    return 'P'
  return 'C'
​
def prime(n):
  if n<2:return False
  return not [i for i in range(2, (n//2) +1) if not n%i]

