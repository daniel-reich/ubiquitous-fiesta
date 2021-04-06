
def is_harshad(num):
  if num != 0:
    sdigit = sum([int(i) for i in str(num) ])
    return num % sdigit == 0
  return False

