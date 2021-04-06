
def add_odd_to_n(n):
  total = []
  for num in range(n+1):
    if num % 2 != 0:
      total.append(num)
  return sum(total)

