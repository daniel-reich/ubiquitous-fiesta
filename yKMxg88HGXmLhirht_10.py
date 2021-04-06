
def add_letters(a):
  if len(a) == 0:
    return 'z'
  x = sum(ord(x) - 96 for x in a)
  x = x + (x//27)
  return chr(x%27 + 96)

