
def check_perfect(num):
  total = 0
  for i in range(1, num):
    if(num % i == 0):
      total += i
  if(num == total):
    return True
  return False

