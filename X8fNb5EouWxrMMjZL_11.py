
def collatz(num):
  r = 0
  while num != 1:
    if num%2:
      num = num*3+1
    else:
      num //= 2
    r += 1
  return r

