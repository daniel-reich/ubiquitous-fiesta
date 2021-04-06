
def even_or_odd(s):
  diff = sum(int(i) for i in s if not int(i) % 2) - sum(int(i) for i in s if int(i) % 2)
  return 'Even is greater than Odd' if diff > 0 else \
    'Odd is greater than Even' if diff < 0 else 'Even and Odd are the same'

