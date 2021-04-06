
def get_birthday_cake(name, age):
  if age%2==0:
    sym = '#'
  else:
    sym = '*'
  ln = '{0} {1} Happy Birthday {2}! {1} {0}'.format(sym,age,name)
  return [sym*len(ln),ln,sym*len(ln)]

