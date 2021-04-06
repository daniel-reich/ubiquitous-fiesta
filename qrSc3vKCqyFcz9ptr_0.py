
def sum_round(num):
  lst = [i for i in str(num)][::-1]
  return ' '.join([i + '0' * idx for idx, i in enumerate(lst) if i != '0'])

