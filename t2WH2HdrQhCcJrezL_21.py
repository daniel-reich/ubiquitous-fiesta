
def eda_bit(start, end):
  return["EdaBit" if (i%3==0) and (i%5==0) or (i==0)  else "Eda" if not i%3 else "Bit" if not i%5 else i for i in range(start,end+1)]

