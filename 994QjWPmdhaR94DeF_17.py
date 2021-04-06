
def get_birthday_cake(name, age):
  d = '#' if age % 2 == 0 else '*'
  return [d * (22 + len(name) + len(str(age)) * 2), d + ' ' + str(age) + " Happy Birthday " + name + '! ' + str(age) + ' ' + d, d * (22 + len(name) + len(str(age)) * 2)]

