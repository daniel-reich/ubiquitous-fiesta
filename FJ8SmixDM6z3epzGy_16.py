
def check_perfect(num):
  factor = sorted([i for i in range(1, num//2 + 1) if num % i == 0], reverse=True)
  return num == sum(factor)

