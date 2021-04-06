
def is_pandigital(n):
  num_str = str(n)
  count = 0
  for i in range(0, 10):
    if num_str.count("{}".format(i)) >= 1:
      count += 1
  if count == 10:
    return True
  else:
    return False

