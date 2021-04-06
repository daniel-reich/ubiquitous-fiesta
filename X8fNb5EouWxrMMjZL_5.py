
def collatz(num):
  count = 1
  if (num / 2) != 1:
    while (num / 2) != 1:
      if (num % 2) != 0:
        num = num * 3 + 1
        count += 1
      else: 
        num = num / 2
        count += 1
    return count
  else:
    return count

