
def return_end_of_number(c):
  if str(c).endswith('11') or str(c).endswith('12') or str(c).endswith('13'):
    return str(c) + '-TH'
  d = {'1': 'ST', '2': 'ND', '3': 'RD'}
  return '{}-{}'.format(c, d[str(c)[-1]]) if str(c)[-1] in d else str(c) + '-TH'

