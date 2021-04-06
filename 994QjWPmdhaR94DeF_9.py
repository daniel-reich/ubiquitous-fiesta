
def get_birthday_cake(name, age):
  if age % 2 == 0:
    ch = '#'
  else:
    ch = '*'
  s = '{} {} Happy Birthday {}! {} {}'.format(ch, str(age), name, str(age), ch)
  l = len(s)
  return [l*ch, s, l*ch]

