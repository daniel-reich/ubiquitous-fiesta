
def return_end_of_number(num):
  d = {'1':'ST', '2':'ND', '3':'RD'}
  s = str(num)
  if num > 10 and s[-2] == '1':
    return '{}-TH'.format(num)
  else:
    return '{}-{}'.format(num, d.get(s[-1], 'TH'))

