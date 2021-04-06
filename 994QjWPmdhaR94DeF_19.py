
def get_birthday_cake(name, age):
  a = '#' if age%2==0 else '*'
  b = '{} {} Happy Birthday {}! {} {}'.format(a, age, name, age, a)
  return [a*len(b), b, a*len(b)]

