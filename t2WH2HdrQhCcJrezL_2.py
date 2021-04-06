
def eda_bit(start, end):
  return ['EdaBit' if not i%3 and not i%5 else 'Eda' if not i%3 else 'Bit' if not i%5 else i for i in range(start, end+1)]

