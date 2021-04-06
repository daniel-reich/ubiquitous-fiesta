
def is_harshad(num):
  try:
    return not bool(num % sum(int(x) for x in str(num)))
  except ZeroDivisionError:
    return False

