
def check_perfect(num):
  factors = [i for i in range(1, 1 + num // 2) if num % i == 0]
  return num == sum(factors)

