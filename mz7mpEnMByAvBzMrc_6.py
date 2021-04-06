
def power_of_two(num):
  i = -1
  while 2 ** i <= num:
    i += 1
    if 2 ** i == num:
      return True
  return False

