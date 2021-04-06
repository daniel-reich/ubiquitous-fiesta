
def eda_bit(start, end):
  return ["EdaBit" if i % 15 == 0 else "Eda" if i % 3 == 0 else "Bit" if i % 5 == 0 else i for i in range(start, end + 1)]

