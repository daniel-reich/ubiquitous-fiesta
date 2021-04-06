
def increment_string(txt):
  if not txt[-1].isnumeric(): return txt + '1'
  i = 0
  for i in range(1, len(txt) + 1):
    if not txt[-i:].isnumeric(): break
  i -= 1
  string = txt[:-i]
  number = str(int(txt[-i:]) + 1)
  return string + '0' * max(len(txt) - len(number) - len(string), 0) + number

