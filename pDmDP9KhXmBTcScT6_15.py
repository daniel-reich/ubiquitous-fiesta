
def get_name(address):
  name = ''
  for x in address:
    if x.isalpha():
      name = name + x
    elif x == '@':
      return name
  return name

