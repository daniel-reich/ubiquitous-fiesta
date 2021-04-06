
def eda_bit(start,end):
  final=[]
  for i in range(start, end+1):
    if i % 3 == 0 and i % 5 == 0:
      final.append("EdaBit")
    elif i % 3 == 0:
      final.append("Eda")
    elif i % 5 == 0:
      final.append("Bit")
    else:
      final.append(i)
  return final

