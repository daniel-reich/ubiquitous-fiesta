
def collatz(num):
  count = 0
  while num != 1:
    count += 1
    if num %2 == 0:
      num /= 2
    elif num%2 == 1:
      num = (num*3) +1
  return count

