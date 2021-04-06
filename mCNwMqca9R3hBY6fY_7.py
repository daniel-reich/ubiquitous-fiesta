
def make_happy(txt):
  return ''.join(')' if txt[i] == '(' and i > 0 and txt[i-1] in ';:8x' else txt[i] for i in range(len(txt)))

