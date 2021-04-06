
def eda_bit(start, end):
  return ["EdaBit" if not n % 3 and not n % 5 else "Eda" if not n % 3 else "Bit" if not n % 5 else n for n in range(start, end + 1)]

