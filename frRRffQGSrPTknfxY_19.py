
def digit_count(n):
  n = str(n)
  return int(''.join([str(n.count(i)) for i in n]))

