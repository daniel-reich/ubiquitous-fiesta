
def is_super_d(n):
  for x in range(2,10):
    if str(x)*x in str(x * n**x):
      return 'Super-{} Number'.format(x)
  return 'Normal Number'

