
def is_repeated(strn):
  for n in (1, 2, 3, 4, 6, 8, 12):
    lst = [strn[i:i + n] for i in range(0, 24, n)]
    if all(map(lambda x: x == lst[0], lst[1:])):
      return 24 // n
  return False

