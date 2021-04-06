
def return_end_of_number(n):
  return '{}{}'.format(n, ['', '-ST', '-ND', '-RD', '-TH'][-1 if 3 < n % 100 < 20 else n % 10])

