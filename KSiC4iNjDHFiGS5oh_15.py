
def is_super_d(n):
  for d in range(2,10):
    if d * str(d) in str(d*n**d):
      return 'Super-{} Number'.format(d)
  return 'Normal Number'

