
def count_digits(lst, t):
  chars = '13579' if t == 'odd' else '02468'
  return [sum(i in chars for i in str(num)) for num in lst]

