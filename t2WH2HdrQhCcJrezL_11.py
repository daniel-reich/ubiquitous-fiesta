
def eda_bit(start, end):
  s = []
  for i in range(start,end+1):
    if i%3==0 and i%5==0:
      s.append('EdaBit')
    elif i%3==0:
      s.append('Eda')
    elif i%5==0:
      s.append('Bit')
    else:
      s.append(i)
  return s

