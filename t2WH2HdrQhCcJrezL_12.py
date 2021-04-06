
def eda_bit(start, end):
  return_statement = []
  for dig in range(start, end+1):
    if dig % 3 == 0 and dig % 5 == 0:
      return_statement.append('EdaBit')
    elif dig % 3 == 0:
      return_statement.append('Eda')
    elif dig % 5 == 0:
      return_statement.append('Bit')
    else:
      return_statement.append(dig)
  return return_statement

