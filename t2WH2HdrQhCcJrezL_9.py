
def eda_bit(start, end):
  lst = []
  for n in range(start, end + 1):
    if n % 3 == 0 and n % 5 == 0:
      lst.append("EdaBit")
    elif n % 3 == 0:
      lst.append("Eda")
    elif n % 5 == 0:
      lst.append("Bit")
    else:
      lst.append(n)
  return lst

