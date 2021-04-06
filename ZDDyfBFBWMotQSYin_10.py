
def is_harshad(num):
  if num == 0: return 0
  return not num % sum([int(c) for c in str(num)])

