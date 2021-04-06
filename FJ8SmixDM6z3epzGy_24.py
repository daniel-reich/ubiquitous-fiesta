
def check_perfect(num):
  factors = [1]
  for i in range(2, num):
    if num % i == 0:
      factors.append(i)
  return sum(factors) == num

