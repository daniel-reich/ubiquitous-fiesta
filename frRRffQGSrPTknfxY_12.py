
def digit_count(n):
  return int(''.join(str(str(n).count(x)) for x in str(n)))

