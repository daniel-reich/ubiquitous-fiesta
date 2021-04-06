
def max_collatz(num):
  highest = num
  while num != 1:
    if num % 2 == 0:
      num = num / 2
    else:
      num = num * 3 + 1
    highest = max(highest, num)
  return highest

