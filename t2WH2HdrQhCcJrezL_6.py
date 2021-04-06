
def eda_bit(start, end):
  temp = []
  for i in range(start,end+1):
    if i % 15 == 0:
      temp.append('EdaBit')
    elif i % 5 == 0:
      temp.append('Bit')
    elif i % 3 == 0:
      temp.append('Eda')
    else:
      temp.append(i)
  return temp

