
def wrap_around(string, offset):
  return string[offset%len(string):] + string[:offset%len(string)]

