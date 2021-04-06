
def eda_bit(start, end):
  lst = []
  for i in range(start, end + 1):
    if i % 15 == 0:
      lst.append('EdaBit')
    elif i % 3 == 0:
      lst.append('Eda')
    elif i % 5 == 0:
      lst.append('Bit')
    else:
      lst.append(i)
  return lst

