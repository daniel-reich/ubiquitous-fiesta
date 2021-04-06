
def add_letters(a):
  if a == []:
    return 'z'
  res = sum(map(lambda c: ord(c) - 96, a))
  while res > 26:
    res -= 26
  return chr(res + 96)

