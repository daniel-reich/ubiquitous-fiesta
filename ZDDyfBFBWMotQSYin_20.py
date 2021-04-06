
def is_harshad(num):
  return False if num == 0 else not num % sum([int(n) for n in str(num)])

