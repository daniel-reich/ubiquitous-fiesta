
def is_harshad(n):
  return not n % sum(map(int, str(n)))

