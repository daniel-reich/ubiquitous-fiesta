
def collatz(num):
  counter = 0
  while num>1:
    if num%2:
      num = num *3 + 1
    else:
      num = num/2
    counter += 1
  return counter

