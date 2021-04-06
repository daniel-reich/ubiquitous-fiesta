
def max_collatz(num):
  numbers = [num]
  while num != 1:
    if num % 2 == 0:
      num = num / 2
      numbers.append(num)
    else:
      num = num * 3 + 1
      numbers.append(num)
  return max(numbers)

