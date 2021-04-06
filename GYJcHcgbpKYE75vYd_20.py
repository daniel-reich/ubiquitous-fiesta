
def return_end_of_number(num):
  n = str(num)
  return '{}-{}'.format(num, 'ST' if n.endswith('1') and not n.endswith('11') else 'ND' if n.endswith('2') and not n.endswith('12') else 'RD' if n.endswith('3') and not n.endswith('13') else 'TH')

