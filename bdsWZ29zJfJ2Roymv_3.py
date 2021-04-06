
def swap_two(txt):
  swapped = ''
  for i in range(0, len(txt), 4):
    a, b = txt[i+2:i+4], txt[i:i+2]
    swapped += (b + a) if len(a + b) < 4 else (a + b)
  return swapped

