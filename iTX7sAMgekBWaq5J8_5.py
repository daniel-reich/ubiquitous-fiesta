
def add_up_to(n):
  numbers = []
  for i in range(n+1):
    if n == 1:
      return 1
    else:
      numbers.append(i)
  return sum(numbers)

