
def wrap_around(string, offset):
  offset %= len(string)
  return string[offset:] + string[:offset]

