
def wrap_around(string, offset):
  if abs(offset) < len(string):
    return string[offset:] + string[:offset]
  else:
    b = offset % len(string)
    return string[b:] + string[:b]

