
def check_perfect(num):
  return sum(x for x in range(1,(num//2)+1) if not num%x) == num

