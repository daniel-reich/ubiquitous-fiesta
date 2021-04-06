
def eda_bit(start, end):
  edabit = []
  for x in range(start, end+1):
    if x % 3 == 0 and x % 5 == 0:
      edabit.append("EdaBit")
    elif x % 3 == 0:
      edabit.append("Eda")
    elif x % 5 == 0:
      edabit.append("Bit")
    else:
      edabit.append(x)
  return edabit

