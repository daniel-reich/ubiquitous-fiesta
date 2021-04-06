
def round_number(num, n):
  a=[(num//n-1)*n, (num//n)*n, (num//n+1)*n]
  b=[abs((num//n-1)*n-num),abs((num//n)*n-num),abs((num//n+1)*n-num)]
  dct={b[i] : a[i] for i in range(len(a))}
  return dct[min(dct.keys())]

