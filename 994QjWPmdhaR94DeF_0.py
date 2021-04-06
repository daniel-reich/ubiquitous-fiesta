
def get_birthday_cake(name, age):
  char = ['#', '*'][age%2]
  msg = '{0} {1} Happy Birthday {2}! {1} {0}'.format(char, age, name)
  wall = char * len(msg)
  return [wall, msg, wall]

