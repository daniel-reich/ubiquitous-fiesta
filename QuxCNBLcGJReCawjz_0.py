
def palindrome_type(n):
  s = 0
  pal = lambda s : s == s[::-1]
  if pal(str(n)):
    s += 1
  if pal(format(n, 'b')):
    s += 2
  return ['Neither!','Decimal only.','Binary only.','Decimal and binary.'][s]

