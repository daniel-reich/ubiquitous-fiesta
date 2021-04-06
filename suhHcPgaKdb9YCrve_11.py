
def even_or_odd(s):
  c = sum(int(x) if int(x) % 2 == 0 else -int(x) for x in s)
  return ['Even and Odd are the same', 'Even is greater than Odd', 'Odd is greater than Even'][(c >= 0) - (c <= 0)]

