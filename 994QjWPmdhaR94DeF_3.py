
def get_birthday_cake(name, age):
  a = ('#','*')[age % 2]
  b = "{0} {1} Happy Birthday {2}! {1} {0}".format(a, age, name)
  return [a*len(b), b, a*len(b)]

