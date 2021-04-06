
def is_boiling(temp):
  print(int(temp[0: len(temp) - 1]))
  return int(temp[0: len(temp) - 1]) >= (100 if temp.endswith('C') else 212)

