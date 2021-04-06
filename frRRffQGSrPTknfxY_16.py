
def digit_count(n):
  return int("".join([str(str(n).count(i)) for i in str(n)]))

