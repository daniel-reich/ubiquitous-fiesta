
def eda_bit(start, end):
  return ['EdaBit' if x % 15 == 0 or x == 0 else 'Eda' if x % 3 == 0 else 'Bit' if x % 5 == 0 else x for x in range(start, end + 1)]

