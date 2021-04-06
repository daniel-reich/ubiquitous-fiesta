
def is_super_d(n):
  for d in range(2, 10):
    value = d * n ** d
    if str(d)*d in str(value):
      return 'Super-%s Number' % d
  return 'Normal Number'

