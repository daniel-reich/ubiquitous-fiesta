
def eda_bit(start, end):
  return ["Eda" if isinstance(c,int) and c%3==0 else c for c in ["Bit" if isinstance(b,int) and b%5==0 else b for b in ["EdaBit" if a%15==0 else a for a in range(start,end+1)]]]

