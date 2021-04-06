
def check_perfect(num):
  return sum([n for n in range(1, (num // 2)+1) if num % n == 0]) == num

