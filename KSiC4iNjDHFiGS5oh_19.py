
import itertools
def is_super_d(n):
  for i in range(2,10):
    number = str(i * n**i)
    for group,number in itertools.groupby(number):
      if group == str(i) and len(list(number)) == i:
        return 'Super-{} Number'.format(i)
  return 'Normal Number'

