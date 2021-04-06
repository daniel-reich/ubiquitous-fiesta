
def is_harshad(num):
  if num == 0:
    return False
  return num % sum([int(x) for x in str(num)]) == 0

