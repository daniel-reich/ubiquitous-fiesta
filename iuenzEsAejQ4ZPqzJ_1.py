
def mystery_func(num):
  int_root = int(num**0.5)
  return int('2' * int_root + str(num - 2**int_root))

