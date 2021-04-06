
d = '0123456789'
def replace_nums(s):
  o = ''
  n = ''
  for x in s:
    if x in d:
      n += x
    else:
      if n != '':
        o += str(bin(int(n)))[2:]
      o += x
      n = ''
  return o

