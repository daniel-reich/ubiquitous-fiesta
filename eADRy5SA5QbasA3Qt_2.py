
def is_harshad(n):
  return n % sum(int(x) for x in str(n)) == 0

