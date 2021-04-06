
def sum_round(num):
  return ' '.join(j + '0' * i for i, j in enumerate(str(num)[::-1]) if j != '0')

