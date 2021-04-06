
def is_prime(numbers: list, n: int):
  while len(numbers) > 1:
    middle = len(numbers) // 2
    if numbers[middle] <= n:
      numbers = numbers[middle:]
    else:
      numbers = numbers[:middle]
  return "yes" if n == numbers[0] else "no"

