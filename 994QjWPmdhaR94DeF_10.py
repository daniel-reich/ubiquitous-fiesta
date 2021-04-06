
def get_birthday_cake(name, age):
  c = '*' if age % 2 == 1 else '#'
  s = "{0} {1} Happy Birthday {2}! {1} {0}".format(c, age, name)
  return [c*len(s), s, c*len(s)]

