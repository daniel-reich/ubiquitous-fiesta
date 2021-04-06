
def wrap_around(string, offset):
  o=offset%len(string)
  return string[o:]+string[:o]

