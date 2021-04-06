
def is_harshad(n):
  return not n % sum(int(i) for i in str(n))

