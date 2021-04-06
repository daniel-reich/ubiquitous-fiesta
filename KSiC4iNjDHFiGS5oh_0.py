
def is_super_d(n):
  for d in range(2, 10):
    if str(d) * d in str(d * n**d):
      return 'Super-{} Number'.format(d)
  return 'Normal Number'

